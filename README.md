# physiometric.app

PosMetric'in tanıtım sitesi. GitHub Pages'ten düz HTML olarak yayınlanır; derleme adımı yoktur.

## Sayfalar

Dört dil (kök Türkçe, `en/`, `de/`, `es/`) × beş sayfa: `index`, `privacy`, `terms`, `delete-account`, `developer`. Ayrıca `404.html`, `sitemap.xml`, `robots.txt`.

Sayfalar elle düzenlenmez; `tools/` altındaki betikle üretilir:

```bash
python3 tools/build_site.py
```

- Metinler: `tools/content.py` (dil kuralları dosyanın başında).
- Şablon: `tools/build_site.py`.
- Stil: `assets/css/site.css` (açık ve koyu tema, uygulamanın renkleri).

Sayfa adresleri değişmemeli; mağaza kayıtları ve uygulama bu adreslere bağlanıyor. `.well-known/assetlinks.json` ve `CNAME` dosyalarına dokunulmaz.

## Koçunla tanış (3D)

`assets/js/coach.js`, ziyaretçi "Canlı göster"e basınca three.js'i (`assets/vendor/three`, r170) ve koç modelini yükler; sayfa açılışında hiçbir model inmez.

- Dört koç, uygulamadaki gibi iki beden × iki görünüm: Elif, Defne, Asım, Kerem. `assets/models/elif.glb` ve `asim.glb` uygulamadaki koçlardan (`physio_metric/assets/3d_animations/koc_sports_*.glb`) web için küçültülmüş kopyalar; Defne Elif'in, Kerem Asım'ın modelini kullanır, yalnızca gövde ve baş dokusu değişir (`assets/models/{defne,kerem}_{body,head}.webp`, uygulamadaki `dokular/*_color1.jpg`'den 1024 px). Üç hareket (shoulder elevation, glute bridge, cat-cow) ve bekleme duruşu kaldı; yatak ve rengi (grafit) uygulamadaki gibi, sopa ve duvar çıkarıldı. Neck lateral stretch, tanıtım sesindeki iddia cümlesi yüzünden sitede yok. Yeniden üretmek için:
  ```bash
  python3 tools/koc_modeli.py <uygulama>/assets/3d_animations/koc_sports_female_01.glb assets/models/elif.glb
  npx -y @gltf-transform/cli@4 prune assets/models/elif.glb assets/models/elif.glb   # sonra webp, meshopt
  ```
- Sesler koçun bedenine göre: Defne Elif'in, Kerem Asım'ın seslerini çalar (`coach.js` → `MODEL`).
- `assets/audio/{dil}/{elif|asim}/guide/`: rehberlik, uygulamanın tanıtım (`intro`) sesleri; hareketi anlatır.
- `assets/audio/{dil}/{elif|asim}/company/`: eşlik, uygulamanın koçluk (`coaching`) sesleri; koç hareketi kullanıcıyla birlikte yapar ve sayar.
- Dosya adlarındaki `elif` ve `asim` yalnızca kimliktir; ekranda görünen ad dile göre değişir (TR Elif/Asım, EN Emma/Jack, DE Anna/Max, ES Lucía/Carlos; `tools/content.py`).
- `assets/img/coach-*-idle.webp`: uygulamanın boy görselleri (`assets/images/coach/koc_*_boy.webp`), aynı ölçekte. `og-*.jpg`: `python3 tools/og_gorselleri.py <koclar_grup.png>` ile çizilir (uygulamanın mağaza görsellerindeki dört koç).
- `assets/img/paket/`: uygulamanın paket görselleri (8 paket × 4 koç), seçili koça göre değişir.

## Karşılama ve mini kontrol

Karşılamada (en üst) ölçüm canlandırması var: önden ve yandan iki örnek fotoğraf (`assets/img/hero-front.webp`, `hero-side.webp`; uygulamanın demo görselinden bölündü). Gövde, el ve ayak noktaları poz modelinin (Pose Landmarker heavy) bu fotoğraflardaki çıktısı; yüz noktaları (burun, gözler, kulaklar, ağız) elle yerleştirildi, çünkü model bu görselde kulakları yüzün içine kaydırıyor. Sonuçlar bu noktalardan uygulamanın formülleriyle hesaplandı: önden baş 0° ve omuz farkı %0,5 (bulgu yok, güçlü yan omuz), yandan çekül hattına göre kulak %12,9 önde (İleri baş duruşu). Konumlar `tools/build_site.py` → `hero_demo` içinde; fotoğraf değişirse yeniden çıkarılıp hesaplanır. Hareket azaltma ayarında canlandırma durur, son kare görünür.

Mini kontrol anasayfada "Koçunla tanış"tan önce (`#try`, menüde "Dene") ve tek başına `/mini-check.html`'de (paylaşmak için; içerik aynı olduğu için `noindex`, site haritasında yok). Uygulamadaki ön çekimin tarayıcıdaki demosu; amacı sistemin çalıştığını göstermek ve uygulamaya yönlendirmek.

- Poz modeli MediaPipe Pose Landmarker (lite) tarayıcıda çalışır: `assets/vendor/mediapipe` (tasks-vision 1.1.0, WebAssembly + WebGL, GPU yoksa CPU), `assets/models/pose_landmarker_lite.task`. Görüntü cihazdan çıkmaz.
- Akış uygulamadaki gibi (`assets/js/check.js` başındaki dosya listesi): yönlendirme (görünürlük → yön → mesafe → ortalama), 2 sn sabit durunca kendiliğinden yakalama, koçun sesli uyarıları ve bekleme kuralları, baş eğikliği ve omuz yükseklik farkı formülleri ve eşikleri. Uygulamada değişirse burası da güncellenir.
- Sesler: `assets/audio/{dil}/{elif|asim}/feedback/`, uygulamanın analiz uyarıları.
- Sonuç ücretsiz sürümdeki gibi: alanın adı ve gözlem cümlesi, ayrıntı "Pro" kilitli, güçlü yan. Altında "Uygulamada seni neler bekliyor?" bölümü ve mağaza düğmeleri.
- Metinler uygulamanın ARB metinleri (`tools/content.py` → `CHECK`).

Tema cihaz ayarına uyar; menüdeki düğmeyle açık ya da koyu seçilebilir (`assets/js/site.js`, seçim tarayıcıda saklanır).

Yazı tipi (Inter) ve three.js siteye gömülüdür; ziyaretçinin bilgisi üçüncü taraf bir sunucuya gitmez.

## Lisanslar

Koç karakterleri Microsoft Rocketbox (MIT, © 2020 Microsoft), three.js (MIT), MediaPipe Tasks Vision ve Pose Landmarker modeli (Apache 2.0), Inter (SIL OFL 1.1).
