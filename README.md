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

- `assets/models/elif.glb`, `asim.glb`: uygulamadaki koçlardan (`physio_metric/assets/3d_animations/koc_sports_*.glb`) web için küçültülmüş kopyalar. Üç hareket (shoulder elevation, glute bridge, cat-cow) ve bekleme duruşu kaldı; yatak modelin içinde, sopa ve duvar çıkarıldı. Neck lateral stretch, tanıtım sesindeki iddia cümlesi yüzünden sitede yok. Dokular 1024 px WebP, geometri ve animasyon meshopt ile sıkıştırıldı (gltf-transform). Hareket etmeyen kanallar yalnızca değerleri düğümün varsayılanına eşitse atıldı (sabit ama farklı değerler uygulamada anlam taşıyor).
- `assets/audio/{dil}/{elif|asim}/guide/`: rehberlik, uygulamanın tanıtım (`intro`) sesleri; hareketi anlatır.
- `assets/audio/{dil}/{elif|asim}/company/`: eşlik, uygulamanın koçluk (`coaching`) sesleri; koç hareketi kullanıcıyla birlikte yapar ve sayar.
- Dosya adlarındaki `elif` ve `asim` yalnızca kimliktir; ekranda görünen ad dile göre değişir (TR Elif/Asım, EN Emma/Jack, DE Anna/Max, ES Lucía/Carlos; `tools/content.py`).
- `assets/img/coach-*-idle.webp`, `og-*.jpg`: modellerden çizilmiş görseller.

## Karşılama ve mini kontrol

Karşılamada (en üst) ölçüm canlandırması var: `assets/img/hero-check.webp` (ödeme ekranı için üretilmiş görsel, üstü kırpıldı) üzerinde poz modelinin bu fotoğraftaki gerçek noktaları ve uygulamanın formülüyle çıkan gerçek sonuç ("Başın dik ve ortada duruyor", baş eğikliği -0,6°). Noktalar `tools/build_site.py` → `hero_demo` içinde; fotoğraf değişirse model yeniden çalıştırılıp güncellenir. Hareket azaltma ayarında canlandırma durur, son kare görünür.

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
