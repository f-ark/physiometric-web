// Mini kontrol: kamera görüntüsünden baş eğikliği ve omuz yükseklik farkı.
// Poz modeli (MediaPipe Pose Landmarker, 33 nokta) tarayıcıda çalışır; görüntü hiçbir yere gitmez.
// Formüller ve eşikler uygulamadakiyle aynıdır (physio_metric):
//   lib/features/analisis/domain/hesaplamalar/bas_egikligi_hesaplama.dart
//   lib/features/analisis/domain/hesaplamalar/omuz_yukseklik_farki_hesaplama.dart
//   lib/features/analisis/domain/durus_bozuklugu_turleri_enum.dart (esikler.hafif)
const root = document.querySelector('[data-check]');
if (root) init(root);

const HEAD_TILT_DEG = 3;     // basEgikligi.esikler.hafif
const SHOULDER_RATIO = 0.02; // omuzYukseklikFarki.esikler.hafif
const MIN_VISIBILITY = 0.5;
const SAMPLE_MS = 1500;     // en az bu kadar süre
const SAMPLE_MAX_MS = 5000; // yavaş cihazlarda en fazla bu kadar beklenir
const SAMPLE_FRAMES = 10;   // en az bu kadar kare
const L = { leftEar: 7, rightEar: 8, leftShoulder: 11, rightShoulder: 12, leftAnkle: 27, rightAnkle: 28 };
const BONES = [[11, 12], [11, 13], [13, 15], [12, 14], [14, 16], [11, 23], [12, 24], [23, 24],
  [23, 25], [25, 27], [24, 26], [26, 28], [7, 8]];

function init(root) {
  const t = JSON.parse(root.dataset.t);
  const video = root.querySelector('video');
  const canvas = root.querySelector('canvas');
  const ctx = canvas.getContext('2d');
  const status = root.querySelector('.status');
  const startBtn = root.querySelector('[data-start]');
  const measureBtn = root.querySelector('[data-measure]');
  const results = root.querySelector('.results');
  const cards = results.querySelector('.cards');
  let landmarker = null;
  let last = null;      // son karedeki noktalar
  let samples = null;   // ölçüm sırasında toplanan kareler
  let sampleStart = 0;

  if (!navigator.mediaDevices?.getUserMedia || typeof WebAssembly !== 'object') {
    status.textContent = t.unsupported;
    startBtn.hidden = true;
    return;
  }

  startBtn.addEventListener('click', async () => {
    startBtn.disabled = true;
    status.textContent = t.loading;
    try {
      const [stream, lm] = await Promise.all([
        navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user', width: { ideal: 1280 }, height: { ideal: 720 } }, audio: false }),
        createLandmarker(),
      ]);
      landmarker = lm;
      video.srcObject = stream;
      await video.play();
    } catch (e) {
      console.error(e);
      status.textContent = e && e.name && /NotAllowed|NotFound|NotReadable|Overconstrained|Security/.test(e.name) ? t.cam_error : t.unsupported;
      startBtn.disabled = false;
      return;
    }
    startBtn.hidden = true;
    measureBtn.hidden = false;
    root.classList.add('live');
    status.textContent = t.ready;
    requestAnimationFrame(loop);
  });

  measureBtn.addEventListener('click', () => {
    measureBtn.disabled = true;
    results.hidden = true;
    status.textContent = t.hold;
    samples = [];
    sampleStart = performance.now();
  });

  let lastTime = -1;
  function loop() {
    if (video.readyState >= 2 && video.currentTime !== lastTime) {
      lastTime = video.currentTime;
      const res = landmarker.detectForVideo(video, performance.now());
      last = res.landmarks?.[0] || null;
      if (samples && last) samples.push(toPixels(last));
      draw();
    }
    if (samples) {
      const ms = performance.now() - sampleStart;
      if ((ms >= SAMPLE_MS && samples.length >= SAMPLE_FRAMES) || ms >= SAMPLE_MAX_MS) finish();
    }
    requestAnimationFrame(loop);
  }

  // Uygulamadaki gibi piksel koordinatlarıyla çalışılır (en/boy oranı korunur).
  function toPixels(pts) {
    const w = video.videoWidth, h = video.videoHeight;
    return pts.map((p) => ({ x: p.x * w, y: p.y * h, v: p.visibility ?? 1 }));
  }

  function draw() {
    const w = video.videoWidth, h = video.videoHeight;
    if (canvas.width !== w) { canvas.width = w; canvas.height = h; }
    ctx.clearRect(0, 0, w, h);
    if (!last) return;
    const p = toPixels(last);
    const s = Math.max(2, w / 320);
    ctx.lineWidth = s;
    ctx.strokeStyle = 'rgba(76,201,240,.9)';
    for (const [a, b] of BONES) {
      if (p[a].v < MIN_VISIBILITY || p[b].v < MIN_VISIBILITY) continue;
      ctx.beginPath(); ctx.moveTo(p[a].x, p[a].y); ctx.lineTo(p[b].x, p[b].y); ctx.stroke();
    }
    ctx.fillStyle = '#E94560';
    for (const i of Object.values(L)) {
      if (p[i].v < MIN_VISIBILITY) continue;
      ctx.beginPath(); ctx.arc(p[i].x, p[i].y, s * 2.2, 0, Math.PI * 2); ctx.fill();
    }
  }

  function finish() {
    const frames = samples || [];
    samples = null;
    measureBtn.disabled = false;
    measureBtn.textContent = t.again;
    const head = median(frames.map(headTilt).filter((x) => x != null));
    const shoulder = median(frames.map(shoulderDiff).filter((x) => x != null));
    if (head == null && shoulder == null) { status.textContent = t.no_person; return; }
    status.textContent = '';
    cards.replaceChildren(
      card(t.head, head == null ? null : Math.abs(head) > HEAD_TILT_DEG
        ? { seen: t.head_tilt.replace('{direction}', head > 0 ? t.dir_right : t.dir_left), daily: t.head_daily }
        : { strong: t.head_strong }, head == null ? t.no_person : null),
      card(t.shoulders, shoulder == null ? null : Math.abs(shoulder) >= SHOULDER_RATIO
        // İşaret: + ise sol omuz-ayak bileği mesafesi uzun, yani sol omuz yukarıda.
        ? { seen: t.sh_tilt.replace('{highSide}', shoulder > 0 ? t.side_left : t.side_right), daily: t.sh_daily }
        : { strong: t.sh_strong }, shoulder == null ? t.need_full : null),
    );
    results.hidden = false;
    results.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  function card(title, r, empty) {
    const el = document.createElement('article');
    el.className = 'card finding';
    const h = document.createElement('h3');
    h.textContent = title;
    el.append(h);
    if (!r) { el.append(para('muted', empty)); return el; }
    if (r.strong) {
      const s = para('strong', r.strong);
      const b = document.createElement('b'); b.textContent = t.strong_label; s.prepend(b);
      el.append(s);
    } else {
      el.append(row('👀', t.seen, r.seen), row('🗓️', t.daily, r.daily));
    }
    return el;
  }
  const para = (cls, text) => { const p = document.createElement('p'); p.className = cls; p.textContent = text; return p; };
  function row(icon, label, text) {
    const d = document.createElement('div'); d.className = 'row';
    const i = document.createElement('span'); i.className = 'ico'; i.textContent = icon;
    const p = document.createElement('p'); const b = document.createElement('b'); b.textContent = label;
    p.append(b, document.createElement('br'), text);
    d.append(i, p);
    return d;
  }
}

// Baş eğikliği (derece). + → sağ kulak aşağıda (sağa eğik), − → sola eğik.
function headTilt(p) {
  const l = p[L.leftEar], r = p[L.rightEar];
  if (l.v < MIN_VISIBILITY || r.v < MIN_VISIBILITY) return null;
  const dx = r.x - l.x, dy = r.y - l.y;
  if (dx * dx + dy * dy < 25) return null; // kulaklar üst üste: önden bakılmıyor
  return Math.atan2(dy, Math.abs(dx)) * 180 / Math.PI;
}

// Omuz yükseklik farkı: omuz–ayak bileği mesafelerinin farkı / ortalaması.
// İşaretli döner: + → sol mesafe uzun (sol omuz yukarıda).
function shoulderDiff(p) {
  const ids = [L.leftShoulder, L.rightShoulder, L.leftAnkle, L.rightAnkle];
  if (ids.some((i) => p[i].v < MIN_VISIBILITY)) return null;
  const sol = Math.hypot(p[L.leftShoulder].x - p[L.leftAnkle].x, p[L.leftShoulder].y - p[L.leftAnkle].y);
  const sag = Math.hypot(p[L.rightShoulder].x - p[L.rightAnkle].x, p[L.rightShoulder].y - p[L.rightAnkle].y);
  const ort = (sol + sag) / 2;
  return ort > 0 ? (sol - sag) / ort : 0;
}

function median(xs) {
  if (xs.length < 3) return null; // yeterli kare yok
  const s = [...xs].sort((a, b) => a - b);
  return s[Math.floor(s.length / 2)];
}

async function createLandmarker() {
  const { FilesetResolver, PoseLandmarker } = await import('/assets/vendor/mediapipe/vision_bundle.mjs');
  const files = await FilesetResolver.forVisionTasks('/assets/vendor/mediapipe/wasm');
  const make = (delegate) => PoseLandmarker.createFromOptions(files, {
    baseOptions: { modelAssetPath: '/assets/models/pose_landmarker_lite.task', delegate },
    runningMode: 'VIDEO',
    numPoses: 1,
  });
  try { return await make('GPU'); } catch { return make('CPU'); }
}
