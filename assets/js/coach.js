// "Koçunla tanış" bölümü. three.js ve model yalnızca ziyaretçi "Canlı göster"e basınca yüklenir.
// Modeller uygulamadaki koçlardan web için küçültülmüş kopyalardır (assets/models).
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
  let coach = 'elif';
  let scene = null; // three.js tarafı yüklenince dolar
  let loading = null;

  const say = (text, ms = 3200) => {
    bubble.textContent = text;
    bubble.classList.add('show');
    clearTimeout(say.timer);
    say.timer = setTimeout(() => bubble.classList.remove('show'), ms);
  };
  const play = (kind) => {
    const audio = new Audio(`/assets/audio/${lang}/${coach}-${kind}.m4a`);
    audio.play().catch(() => {});
  };

  coachBtns.forEach((b) => b.addEventListener('click', async () => {
    coach = b.dataset.pick;
    coachBtns.forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
    poster.src = `/assets/img/coach-${coach}.webp`;
    poster.alt = b.textContent.trim();
    if (scene) { await start(); greet(); }
  }));

  liveBtn.addEventListener('click', async () => {
    await start();
    greet();
  });

  moveBtns.forEach((b) => b.addEventListener('click', async () => {
    await start();
    const move = b.dataset.move;
    moveBtns.forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
    if (move === 'celebrate_cheer_04') { scene.once(move); say(t.cheer); play('celebration'); }
    else if (move === 'greet_wave_01') greet();
    else scene.loop(move);
  }));

  function greet() {
    scene.once('greet_wave_01');
    say(t.greeting);
    play('greeting');
  }

  async function start() {
    if (scene && scene.coach === coach) return;
    if (loading) return loading;
    status.textContent = t.loading;
    loading = (async () => {
      try {
        if (!scene) scene = await createScene(viewer);
        await scene.load(coach);
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
  let model = null, mixer = null, clips = {}, current = null, bed = [], face = null;
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
    const yaw = BED_MOVES.has(name) ? 0.75 : 0.12;
    const fit = Math.max(s.y, Math.max(s.x, s.z) / camera.aspect) / 2 / Math.tan(THREE.MathUtils.degToRad(15)) * 1.15;
    camera.position.set(c.x + Math.sin(yaw) * fit, c.y + s.y * 0.08, c.z + Math.cos(yaw) * fit);
    controls.target.copy(c); controls.update();
  }

  function run(name, once) {
    const clip = clips[name]; if (!clip) return;
    bed.forEach((m) => { m.visible = BED_MOVES.has(name); });
    const next = mixer.clipAction(clip);
    mixer.stopAllAction();
    next.setLoop(once ? THREE.LoopOnce : THREE.LoopRepeat, Infinity);
    next.clampWhenFinished = true;
    next.play();
    frame(name, next);
    current = next;
  }
  api.loop = (name) => run(name, false);
  api.once = (name) => run(name, true);

  api.load = async (coach) => {
    if (model) { world.remove(model); }
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
    mixer.addEventListener('finished', () => api.loop('idle_breathe_01'));
    current = null;
    api.coach = coach;
    api.loop('idle_breathe_01');
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
