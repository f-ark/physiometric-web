// Mini kontrol: uygulamadaki ön çekimin tarayıcıdaki demosu.
// Poz modeli (MediaPipe Pose Landmarker, 33 nokta) tarayıcıda çalışır; görüntü hiçbir yere gitmez.
// Akış ve sayılar uygulamadakiyle aynıdır (physio_metric, lib/features/analisis/):
//   domain/pose_validation/pose_validator.dart      yönlendirme: görünürlük → yön → mesafe → ortalama
//   domain/pose_validation/stability_validator.dart 2 sn sabit durunca kendiliğinden yakalama
//   application/analysis_voice_feedback_service.dart koçun sesli uyarıları ve bekleme kuralları
//   domain/hesaplamalar/bas_egikligi_hesaplama.dart, omuz_yukseklik_farki_hesaplama.dart
//   domain/durus_bozuklugu_turleri_enum.dart        eşikler (hafif / orta / yüksek)
//   presentation/sonuc/sonuc_ekrani.dart             sonuç, ücretsiz sürümdeki gibi
// Tek fark: uygulama dikey telefon görüntüsü varsayar; burada görüntünün gerçek eni ve boyu kullanılır.
const P = { nose: 0, lEar: 7, rEar: 8, lSh: 11, rSh: 12, lHip: 23, rHip: 24, lKnee: 25, rKnee: 26, lAnk: 27, rAnk: 28 };
const BONES = [[11, 12], [11, 13], [13, 15], [12, 14], [14, 16], [11, 23], [12, 24], [23, 24],
  [23, 25], [25, 27], [24, 26], [26, 28], [7, 8]];

// PoseValidator
const MIN_BODY = 0.40, MAX_BODY = 0.95, FRONT_MIN_SH_TORSO = 0.45, MAX_CENTER_DEV = 0.35, VIS_REQUIRED = 0.30;
const REQUIRED = [P.lSh, P.rSh, P.lHip, P.rHip, P.lEar, P.rEar, P.lKnee, P.rKnee, P.lAnk, P.rAnk];
// StabilityValidator ve LiveFeedbackNotifier
const STABLE_MS = 2000, MIN_FRAMES = 3, FRAME_GAP_MS = 300, UNCLEAR_MS = 3000, VIS_STABLE = 0.5;
const KEY = [P.nose, P.lSh, P.rSh, P.lHip, P.rHip, P.lKnee, P.rKnee, P.lAnk, P.rAnk];
// AnalysisVoiceFeedbackService
const MIN_GAP = 3000, END_GAP = 500, REPEAT_GAP = 6000, MAX_SOUND = 6000;
const NON_REPEATING = new Set(['valid', 'stabilizing', 'capturing_photo']);
// Eşikler ve LandmarkYardimcisi.getLandmark
const HEAD = { hafif: 3, orta: 6, yuksek: 9 };
const SHOULDER = { hafif: 0.02, orta: 0.04, yuksek: 0.06 };
const VIS_CALC = 0.5;
// Renk dili (K-22): turuncu = düzelt, mavi = böyle kal, yeşil = tamam.
const KIND = { stabilizing: 'hold', valid: 'hold', capturing_photo: 'ok' };

function init(root) {
  const t = JSON.parse(root.dataset.t);
  const lang = document.documentElement.lang;
  const $ = (s) => root.querySelector(s);
  const cam = $('.cam'), video = $('.cam video'), canvas = $('.cam canvas'), ctx = canvas.getContext('2d');
  const pill = $('.live-pill'), bar = $('.hold-bar i'), status = $('.cam .status');
  const startBtn = $('[data-start]'), soundBox = $('[data-sound]');
  const results = $('.results'), body = $('.res-body'), shot = $('.shot canvas'), cta = document.querySelector('[data-cta]');
  const coachBtns = [...root.querySelectorAll('[data-pick]')];
  let coach = 'elif';
  let landmarker = null, running = false;
  const stab = new Stability();
  let unclearSince = null, last = null, lastTime = -1, lastUpdate = 0;
  const voice = new Voice(() => `/assets/audio/${lang}/${coach}/feedback/`, () => soundBox.checked);

  coachBtns.forEach((b) => b.addEventListener('click', () => {
    coach = b.dataset.pick;
    coachBtns.forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
  }));
  soundBox.addEventListener('change', () => { if (!soundBox.checked) voice.stop(); });

  if (!navigator.mediaDevices?.getUserMedia || typeof WebAssembly !== 'object') {
    status.textContent = t.unsupported;
    startBtn.hidden = true;
    return;
  }

  startBtn.addEventListener('click', async () => {
    voice.unlock(); // iOS: ses ancak bir dokunuşla açılır
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
      status.textContent = e && /NotAllowed|NotFound|NotReadable|Overconstrained|Security/.test(e.name) ? t.cam_error : t.unsupported;
      startBtn.disabled = false;
      return;
    }
    startBtn.hidden = true;
    status.textContent = '';
    cam.classList.add('live');
    begin();
    requestAnimationFrame(loop);
  });

  $('[data-again]').addEventListener('click', () => {
    results.hidden = true;
    if (cta) cta.hidden = false;
    cam.scrollIntoView({ behavior: 'smooth', block: 'center' });
    begin();
  });

  function begin() {
    stab.reset(); unclearSince = null;
    voice.reset();
    running = true;
    setStatus('pose_not_found');
  }

  function setStatus(s, progress = 0) {
    cam.dataset.kind = KIND[s] || 'fix';
    pill.textContent = t.live[s];
    bar.style.width = s === 'stabilizing' ? `${Math.round(progress * 100)}%` : s === 'capturing_photo' ? '100%' : '0';
    voice.status(s);
  }

  function loop() {
    if (video.readyState >= 2 && video.currentTime !== lastTime) {
      lastTime = video.currentTime;
      const now = performance.now();
      const res = landmarker.detectForVideo(video, now);
      const raw = res.landmarks?.[0];
      last = raw ? toPixels(raw, video.videoWidth, video.videoHeight) : null;
      draw();
      if (running && now - lastUpdate >= 100) { lastUpdate = now; step(now); }
    }
    requestAnimationFrame(loop);
  }

  function step(now) {
    const w = video.videoWidth, h = video.videoHeight;
    const v = last ? validate(last, w, h) : 'pose_not_found';
    if (v !== 'valid') { stab.reset(); unclearSince = null; setStatus(v); return; }
    const r = stab.add(last, now);
    if (r.type === 'accumulating') { unclearSince = null; setStatus('stabilizing', r.progress); }
    else if (r.type === 'moving') {
      unclearSince ??= now;
      setStatus(now - unclearSince > UNCLEAR_MS ? 'pose_not_clear' : 'moving');
    } else if (r.type === 'stable') capture(r.median);
  }

  function capture(median) {
    running = false;
    setStatus('capturing_photo');
    voice.stop();
    voice.say('capturing_photo');
    snapshot(median);
    setTimeout(() => {
      voice.say('analysis_complete');
      showResults(median);
    }, 1200);
  }

  // Sonuç fotoğrafı: kişiye kırpılmış kare, üstünde dikey hat ve ölçülen yatay çizgiler.
  function snapshot(pts) {
    const w = video.videoWidth, h = video.videoHeight;
    const vis = pts.filter((p) => p.v >= VIS_REQUIRED);
    const xs = vis.map((p) => p.x), ys = vis.map((p) => p.y);
    const bh = Math.max(...ys) - Math.min(...ys);
    const pad = bh * 0.12;
    const top = Math.max(0, Math.min(...ys) - pad * 1.6), bottom = Math.min(h, Math.max(...ys) + pad);
    const ch = bottom - top, cw = Math.min(w, ch * 0.62);
    const cx = (Math.min(...xs) + Math.max(...xs)) / 2;
    const left = Math.max(0, Math.min(w - cw, cx - cw / 2));
    const scale = Math.min(1, 900 / ch);
    shot.width = Math.round(cw * scale); shot.height = Math.round(ch * scale);
    const g = shot.getContext('2d');
    g.save();
    g.translate(shot.width, 0); g.scale(-1, 1); // aynadaki gibi
    g.drawImage(video, left, top, cw, ch, 0, 0, shot.width, shot.height);
    const map = (p) => ({ x: (p.x - left) * scale, y: (p.y - top) * scale });
    const head = headTilt(pts), sh = shoulderDiff(pts);
    const lw = Math.max(2, shot.width / 160);
    const ankMid = map(mid(pts[P.lAnk], pts[P.rAnk]));
    g.setLineDash([lw * 3, lw * 2]); g.lineWidth = lw; g.strokeStyle = 'rgba(255,255,255,.9)';
    g.beginPath(); g.moveTo(ankMid.x, shot.height); g.lineTo(ankMid.x, 0); g.stroke();
    g.setLineDash([]);
    const line = (a, b, seen) => {
      const A = map(a), B = map(b), dx = B.x - A.x, dy = B.y - A.y, k = 0.35;
      g.strokeStyle = seen ? '#E94560' : '#22C55E'; g.lineWidth = lw * 1.4;
      g.beginPath(); g.moveTo(A.x - dx * k, A.y - dy * k); g.lineTo(B.x + dx * k, B.y + dy * k); g.stroke();
      g.fillStyle = g.strokeStyle;
      for (const Q of [A, B]) { g.beginPath(); g.arc(Q.x, Q.y, lw * 2.4, 0, Math.PI * 2); g.fill(); }
    };
    if (head) line(pts[P.lEar], pts[P.rEar], head.level != null);
    if (sh) line(pts[P.lSh], pts[P.rSh], sh.level != null);
    g.restore();
  }

  function showResults(pts) {
    const head = headTilt(pts), sh = shoulderDiff(pts);
    const found = [];
    if (head?.level != null) found.push({ name: t.name_head, level: head.level, norm: head.deger / HEAD.hafif,
      text: t.head_tilt.replace('{direction}', head.sapma > 0 ? t.dir_right : t.dir_left) });
    if (sh?.level != null) found.push({ name: t.name_sh, level: sh.level, norm: sh.deger / SHOULDER.hafif,
      // sağ mesafe kısa = sağ omuz aşağıda = sol omuz yukarıda
      text: t.sh_tilt.replace('{highSide}', sh.dusuk === 'sag' ? t.side_left : t.side_right) });
    found.sort((a, b) => b.level - a.level || b.norm - a.norm);
    // Güçlü yan: uygulamadaki bölge sırası (omuz, sonra baş ve boyun); bulgusu olmayan ilk bölge.
    const strong = sh && sh.level == null ? t.sh_strong : head && head.level == null ? t.head_strong : null;

    $('.results .date').textContent = t.res_today.replace('{date}',
      new Intl.DateTimeFormat(lang, { day: 'numeric', month: 'long' }).format(new Date()));
    const out = [];
    if (!found.length) out.push(el('p', 'lead-text', t.no_findings));
    else {
      out.push(el('h3', '', found.length === 1 ? t.top_one : t.top_n.replace('{count}', found.length)));
      found.forEach((f, i) => {
        const c = el('article', 'card area');
        c.append(el('span', 'tag', i ? t.tag2 : t.tag1), el('h4', '', f.name), el('p', '', f.text));
        const lock = el('div', 'lock');
        lock.append(el('span', '', t.locked), el('span', 'pro-tag', 'Pro'));
        c.append(lock);
        out.push(c);
      });
    }
    if (strong) {
      out.push(el('h3', '', t.strong_title));
      const c = el('article', 'card strong-card');
      c.append(el('span', 'ok', '✓'), el('p', '', strong));
      out.push(c);
    }
    out.push(el('p', 'disc', t.disclaimer));
    body.replaceChildren(...out);
    results.hidden = false;
    if (cta) cta.hidden = true;
    results.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function draw() {
    const w = video.videoWidth, h = video.videoHeight;
    if (canvas.width !== w) { canvas.width = w; canvas.height = h; }
    ctx.clearRect(0, 0, w, h);
    if (!last || !running) return;
    const s = Math.max(2, w / 320);
    const color = { fix: '#FF6D00', hold: '#4361EE', ok: '#22C55E' }[cam.dataset.kind] || '#4CC9F0';
    ctx.lineWidth = s; ctx.strokeStyle = color; ctx.fillStyle = color;
    for (const [a, b] of BONES) {
      if (last[a].v < VIS_REQUIRED || last[b].v < VIS_REQUIRED) continue;
      ctx.beginPath(); ctx.moveTo(last[a].x, last[a].y); ctx.lineTo(last[b].x, last[b].y); ctx.stroke();
    }
    for (const i of REQUIRED) {
      if (last[i].v < VIS_REQUIRED) continue;
      ctx.beginPath(); ctx.arc(last[i].x, last[i].y, s * 2, 0, Math.PI * 2); ctx.fill();
    }
  }
}

const el = (tag, cls, text) => {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (text != null) e.textContent = text;
  return e;
};
const mid = (a, b) => ({ x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 });
const dist = (a, b) => Math.hypot(a.x - b.x, a.y - b.y);

// Uygulamadaki gibi piksel koordinatları; v = görünürlük (ML Kit'teki likelihood).
function toPixels(pts, w, h) {
  return pts.map((p) => ({ x: p.x * w, y: p.y * h, v: p.visibility ?? 1 }));
}

// PoseValidator, ön profil.
function validate(p, w, h) {
  if (REQUIRED.some((i) => p[i].v < VIS_REQUIRED)) return 'body_not_visible';
  const shW = dist(p[P.lSh], p[P.rSh]);
  const torso = dist(mid(p[P.lSh], p[P.rSh]), mid(p[P.lHip], p[P.rHip]));
  if (torso >= 1 && shW / torso < FRONT_MIN_SH_TORSO) return 'face_camera';
  const ears = [p[P.lEar], p[P.rEar]].filter((l) => l.v >= VIS_REQUIRED);
  const ankles = [p[P.lAnk], p[P.rAnk]].filter((l) => l.v >= VIS_REQUIRED);
  if (ears.length && ankles.length) {
    const ratio = (Math.max(...ankles.map((l) => l.y)) - Math.min(...ears.map((l) => l.y))) / h;
    if (ratio < MIN_BODY) return 'too_far';
    if (ratio > MAX_BODY) return 'too_close';
  }
  // Görüntü aynalı değil: kişinin sağı görüntünün solunda.
  const dev = (p[P.lHip].x + p[P.rHip].x) / 2 - w / 2;
  if (dev > w * MAX_CENTER_DEV) return 'move_right';
  if (dev < -w * MAX_CENTER_DEV) return 'move_left';
  return 'valid';
}

// StabilityValidator: kişi 2 sn sabit durursa noktaların ortancası alınır.
class Stability {
  constructor() { this.reset(); }
  reset() { this.buf = []; this.lastT = null; this.runStart = null; }
  add(pts, now) {
    if (this.lastT != null && now - this.lastT < FRAME_GAP_MS) return { type: 'waiting' };
    this.lastT = now;
    const f = pts.map((l) => (l.v >= VIS_STABLE ? l : null));
    if (!this.buf.length) this.runStart = now;
    this.buf.push({ f, t: now });
    while (this.buf.length > MIN_FRAMES && now - this.buf[0].t > STABLE_MS) this.buf.shift();
    const elapsed = now - this.runStart;
    const progress = Math.min(1, elapsed / STABLE_MS);
    if (this.buf.length < MIN_FRAMES) return { type: 'accumulating', progress: Math.min(progress, 0.99) };
    const variance = this.variance(KEY);
    const ls = f[P.lSh], rs = f[P.rSh], lh = f[P.lHip];
    const scale = ls && rs && lh ? Math.max(Math.abs(ls.x - rs.x), Math.abs(ls.y - lh.y)) : 0;
    const limit = scale > 0 ? scale * 0.05 : 15;
    if (variance > limit) {
      this.buf.splice(0, Math.ceil(this.buf.length / 2));
      this.runStart = this.buf.length ? this.buf[0].t : null;
      return { type: 'moving' };
    }
    if (elapsed < STABLE_MS) return { type: 'accumulating', progress };
    return { type: 'stable', median: this.median() };
  }
  variance(ids) {
    let total = 0, count = 0;
    for (const i of ids) {
      const seen = this.buf.map((b) => b.f[i]).filter(Boolean);
      if (seen.length >= this.buf.length * 0.7) {
        total += sd(seen.map((l) => l.x)) + sd(seen.map((l) => l.y));
        count += 2;
      }
    }
    return count ? total / count : Infinity;
  }
  median() {
    return this.buf[0].f.map((_, i) => {
      const seen = this.buf.map((b) => b.f[i]).filter(Boolean);
      if (!seen.length) return { x: 0, y: 0, v: 0 };
      return { x: med(seen.map((l) => l.x)), y: med(seen.map((l) => l.y)), v: med(seen.map((l) => l.v)) };
    });
  }
}
function sd(xs) {
  if (xs.length < 2) return 0;
  const m = xs.reduce((a, b) => a + b, 0) / xs.length;
  return Math.sqrt(xs.reduce((a, b) => a + (b - m) ** 2, 0) / xs.length);
}
function med(xs) {
  const s = [...xs].sort((a, b) => a - b), n = s.length >> 1;
  return s.length % 2 ? s[n] : (s[n - 1] + s[n]) / 2;
}
function level(value, e) {
  return value >= e.yuksek ? 2 : value >= e.orta ? 1 : 0;
}

// Baş eğikliği: kulaklar arası açı. sapma > 0 → sağ kulak aşağıda (sağa eğik).
// Strateji: deger > hafif ise bulgu.
function headTilt(p) {
  const l = p[P.lEar], r = p[P.rEar];
  if (l.v <= VIS_CALC || r.v <= VIS_CALC) return null;
  const dx = r.x - l.x, dy = r.y - l.y;
  if (dx * dx + dy * dy < 25) return null;
  const sapma = Math.atan2(dy, Math.abs(dx)) * 180 / Math.PI, deger = Math.abs(sapma);
  return { sapma, deger, level: deger > HEAD.hafif ? level(deger, HEAD) : null };
}

// Omuz yükseklik farkı: omuz–ayak bileği mesafelerinin farkı / ortalaması.
// Strateji: fark < hafif ise bulgu yok.
function shoulderDiff(p) {
  const ids = [P.lSh, P.rSh, P.lAnk, P.rAnk];
  if (ids.some((i) => p[i].v <= VIS_CALC)) return null;
  const sol = dist(p[P.lSh], p[P.lAnk]), sag = dist(p[P.rSh], p[P.rAnk]);
  const ort = (sol + sag) / 2;
  const deger = ort > 0 ? Math.abs(sol - sag) / ort : 0;
  return { deger, dusuk: sag < sol ? 'sag' : 'sol', level: deger >= SHOULDER.hafif ? level(deger, SHOULDER) : null };
}

// Koçun sesli uyarıları. Sesler birbirini kesmez: yeni ses öncekinin başlamasından en az 3 sn,
// bitişinden en az 0,5 sn sonra başlar; bu arada gelen durum bekletilir ve süre dolunca güncel
// durum söylenir. Düzeltme isteyen uyarı sürerse 6 sn'de bir tekrarlanır.
class Voice {
  constructor(base, enabled) {
    this.base = base; this.enabled = enabled;
    this.audio = new Audio();
    this.audio.addEventListener('ended', () => this.ended());
    this.audio.addEventListener('error', () => this.ended());
    this.reset();
    setInterval(() => this.tick(), 200);
  }
  unlock() {
    this.audio.muted = true;
    this.audio.src = `${this.base()}stabilizing.m4a`;
    this.audio.play().then(() => { this.audio.pause(); this.audio.muted = false; })
      .catch(() => { this.audio.muted = false; });
  }
  reset() { this.current = null; this.spoken = null; this.next = null; this.startT = -1e9; this.endT = -1e9; this.speaking = false; }
  status(s) { this.current = s; }
  // Yakalama ve bitiş sesleri: bekleme süresi aranmaz, çalan ses bitince sırayla söylenir.
  say(name) { this.current = null; this.next = name; this.tick(); }
  ended() { if (this.speaking) { this.speaking = false; this.endT = performance.now(); } }
  stop() { this.audio.pause(); this.ended(); }
  play(name) {
    if (!this.enabled()) return;
    this.audio.src = `${this.base()}${name}.m4a`;
    this.audio.play().catch(() => this.ended());
    this.speaking = true; this.startT = performance.now();
  }
  tick() {
    const now = performance.now();
    if (this.speaking && now - this.startT > MAX_SOUND) this.ended();
    if (this.next) {
      if (!this.speaking && now - this.endT >= END_GAP) { this.play(this.next); this.next = null; }
      return;
    }
    const s = this.current;
    if (!s || s === 'valid' || this.speaking || !this.enabled()) return;
    if (now - this.startT < MIN_GAP || now - this.endT < END_GAP) return;
    if (s === this.spoken && (NON_REPEATING.has(s) || now - this.startT < REPEAT_GAP)) return;
    this.spoken = s;
    this.play(s);
  }
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

// Sınıflar ve sabitler tanımlandıktan sonra başlar.
const root = document.querySelector('[data-check]');
if (root) init(root);
