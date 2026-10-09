// "Koçunla tanış" bölümü. three.js ve model yalnızca ziyaretçi "Canlı göster"e ya da bir harekete
// basınca yüklenir. Modeller uygulamadaki koçlardan web için küçültülmüş kopyalardır (assets/models).
// Her hareketin iki sesi var, uygulamadaki gibi: rehberlik hareketi anlatır (tanıtım sesi, intro),
// eşlikte koç hareketi kullanıcıyla birlikte yapar ve sayar (koçluk sesi, coaching).
const box = document.querySelector('[data-coach]');
if (box) init(box);

function init(box) {
  const viewer = box.querySelector('.viewer');
  const poster = viewer.querySelector('.poster');
  const bubble = viewer.querySelector('.bubble');
  const status = viewer.querySelector('.status');
  const lang = document.documentElement.lang;
  const t = box.dataset;
  const coachBtns = [...box.querySelectorAll('[data-pick]')];
  const moveBtns = [...box.querySelectorAll('[data-move]')];
  const liveBtn = box.querySelector('[data-live]');
  const guideBtn = box.querySelector('[data-guide]');
  const companyBtn = box.querySelector('[data-company]');
  let coach = 'elif';
  let move = moveBtns[0].dataset.move;
  let scene = null; // three.js tarafı yüklenince dolar
  let loading = null;
  let audio = null;

  // Ses çalarken balon açık kalır, ses bitince kapanır.
  const speak = (kind, text) => {
    if (audio) audio.pause();
    bubble.textContent = text;
    bubble.classList.add('show');
    audio = new Audio(`/assets/audio/${lang}/${coach}/${kind}/${move}.m4a`);
    clearTimeout(speak.timer);
    const close = () => bubble.classList.remove('show');
    // Ses çalamazsa balon okunacak kadar açık kalır.
    const fallback = () => { speak.timer = setTimeout(close, 2000 + text.length * 50); };
    audio.addEventListener('ended', close, { once: true });
    audio.addEventListener('error', fallback, { once: true });
    audio.play().catch(fallback);
  };
  const stopVoice = () => {
    if (audio) audio.pause();
    clearTimeout(speak.timer);
    bubble.classList.remove('show');
  };
  const pressMove = () => moveBtns.forEach((x) => x.setAttribute('aria-pressed', String(x.dataset.move === move)));
  const current = () => moveBtns.find((x) => x.dataset.move === move);

  coachBtns.forEach((b) => b.addEventListener('click', async () => {
    coach = b.dataset.pick;
    coachBtns.forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
    poster.src = `/assets/img/coach-${coach}-idle.webp`;
    poster.alt = b.textContent.trim();
    // Paket görselleri de uygulamadaki gibi seçili koça göre.
    document.querySelectorAll('img[data-pack]').forEach((img) => {
      img.src = `/assets/img/paket/paket_${img.dataset.pack}_${coach}.webp`;
    });
    stopVoice();
    if (scene) { await start(); scene.loop(move); }
  }));

  liveBtn.addEventListener('click', async () => {
    await start();
    pressMove();
    scene.loop(move);
  });

  moveBtns.forEach((b) => b.addEventListener('click', async () => {
    move = b.dataset.move;
    pressMove();
    stopVoice();
    await start();
    scene.loop(move);
  }));

  guideBtn.addEventListener('click', async () => {
    await start();
    pressMove();
    scene.loop(move);
    speak('guide', current().dataset.guideText);
  });

  companyBtn.addEventListener('click', async () => {
    await start();
    pressMove();
    scene.loop(move); // hareket baştan başlar, koç sesle birlikte yapar
    speak('company', current().dataset.companyText);
  });

  async function start() {
    if (scene && scene.coach === coach) return;
    if (loading) return loading;
    status.textContent = t.loading;
    loading = (async () => {
      try {
        if (!scene) scene = await createScene(viewer);
        await scene.load(coach);
        scene.loop(move);
        viewer.classList.add('live');
        liveBtn.hidden = true;
        status.textContent = '';
      } catch (e) {
        console.error(e);
        status.textContent = t.error;
      } finally {
        loading = null;
      }
    })();
    return loading;
  }
}

async function createScene(viewer) {
  const THREE = await import('three');
  const { GLTFLoader } = await import('/assets/vendor/three/addons/loaders/GLTFLoader.js');
  const { MeshoptDecoder } = await import('/assets/vendor/three/addons/libs/meshopt_decoder.module.js');
  const { OrbitControls } = await import('/assets/vendor/three/addons/controls/OrbitControls.js');

  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  viewer.prepend(renderer.domElement);

  const world = new THREE.Scene();
  world.add(new THREE.HemisphereLight(0xffffff, 0x334466, 2.2));
  const key = new THREE.DirectionalLight(0xffffff, 2.6); key.position.set(3, 5, 4); world.add(key);
  const rim = new THREE.DirectionalLight(0x4cc9f0, 2.2); rim.position.set(-4, 3, -3); world.add(rim);

  const camera = new THREE.PerspectiveCamera(30, 1, 1, 20000);
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableZoom = false; controls.enablePan = false; controls.enableDamping = true;
  controls.minPolarAngle = Math.PI * 0.3; controls.maxPolarAngle = Math.PI * 0.55;

  const loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
  const cache = {};
  const clock = new THREE.Clock();
  let model = null, mixer = null, clips = {}, bed = [], face = null;
  // Yatakta yapılan hareketler; yatak yalnızca bunlarda görünür.
  const BED_MOVES = new Set(['shoulder_elevation', 'neck_lateral_stretch', 'glute_bridge', 'cat_cow']);
  const api = { coach: null };

  function resize() {
    const w = viewer.clientWidth, h = viewer.clientHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h; camera.updateProjectionMatrix();
  }
  new ResizeObserver(resize).observe(viewer);
  resize();

  // Kareye sığdır: hareketin birkaç anındaki kapsayıcı kutu.
  function frame(name, action) {
    const clip = clips[name];
    const box = new THREE.Box3();
    for (const f of [0, 0.25, 0.5, 0.75]) {
      mixer.setTime(clip.duration * f);
      model.updateMatrixWorld(true);
      model.traverse((o) => { if (o.isMesh && o.visible) box.union(new THREE.Box3().setFromObject(o, true)); });
    }
    action.reset();
    const c = box.getCenter(new THREE.Vector3()), s = box.getSize(new THREE.Vector3());
    const yaw = BED_MOVES.has(name) ? 0.75 : 0.35;
    const h = Math.max(s.y, Math.max(s.x, s.z) / camera.aspect);
    const fit = h / 2 / Math.tan(THREE.MathUtils.degToRad(15)) * 1.15;
    camera.position.set(c.x + Math.sin(yaw) * fit, c.y + h * 0.08, c.z + Math.cos(yaw) * fit);
    controls.target.copy(c); controls.update();
  }

  api.loop = (name) => {
    const clip = clips[name]; if (!clip) return;
    bed.forEach((m) => { m.visible = BED_MOVES.has(name); });
    const action = mixer.clipAction(clip);
    mixer.stopAllAction();
    action.setLoop(THREE.LoopRepeat, Infinity);
    action.play();
    frame(name, action);
  };

  api.load = async (coach) => {
    if (model) world.remove(model);
    cache[coach] ??= loader.loadAsync(`/assets/models/${coach}.glb`);
    const gltf = await cache[coach];
    model = gltf.scene;
    model.rotation.y = -Math.PI / 2; // modeller +X yönüne bakıyor
    bed = []; face = null;
    model.traverse((o) => {
      if (!o.isMesh) return;
      o.frustumCulled = false;
      if (/cube/i.test(o.name)) {
        bed.push(o);
        const legs = /_1$/.test(o.name);
        o.material = new THREE.MeshStandardMaterial({ color: legs ? 0x2a3046 : 0xdfe6f2, roughness: 0.85 });
      } else if (o.morphTargetDictionary && 'blink_l' in o.morphTargetDictionary) {
        face = o;
        const d = o.morphTargetDictionary;
        o.morphTargetInfluences[d.smile_l] = o.morphTargetInfluences[d.smile_r] = 0.35;
      }
    });
    world.add(model);
    mixer = new THREE.AnimationMixer(model);
    clips = Object.fromEntries(gltf.animations.map((c) => [c.name, c]));
    api.coach = coach;
  };

  // Göz kırpma: 3–5 saniyede bir.
  let nextBlink = 2, blinkT = -1;
  function blink(dt, now) {
    if (!face) return;
    const d = face.morphTargetDictionary, inf = face.morphTargetInfluences;
    if (blinkT < 0 && now > nextBlink) { blinkT = 0; nextBlink = now + 3 + Math.random() * 2; }
    if (blinkT >= 0) {
      blinkT += dt;
      const v = blinkT < 0.08 ? blinkT / 0.08 : Math.max(0, 1 - (blinkT - 0.08) / 0.1);
      inf[d.blink_l] = inf[d.blink_r] = v;
      if (blinkT > 0.2) blinkT = -1;
    }
  }

  let visible = true;
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; }).observe(viewer);
  renderer.setAnimationLoop(() => {
    const dt = clock.getDelta();
    if (!visible || !mixer) return;
    mixer.update(dt);
    blink(dt, clock.elapsedTime);
    controls.update();
    renderer.render(world, camera);
  });

  return api;
}
