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
- `assets/img/coach-*.webp`, `og-*.jpg`: modellerden çizilmiş görseller.

## Mini kontrol (deneme)

`/mini-check.html` (ve `en/`, `de/`, `es/`): kameradan baş eğikliği ve omuz yükseklik farkı. Menüde ve site haritasında yok, `noindex`; bağlantıyı bilen açar.

- Poz modeli MediaPipe Pose Landmarker (lite) tarayıcıda çalışır: `assets/vendor/mediapipe` (tasks-vision 1.1.0, WebAssembly + WebGL, GPU yoksa CPU), `assets/models/pose_landmarker_lite.task`. Görüntü cihazdan çıkmaz.
- Formüller ve eşikler uygulamadakiyle aynı (`assets/js/check.js` başındaki dosya listesi). Uygulamada değişirse burası da güncellenir.
- Cümleler uygulamanın ARB metinleri (`tools/content.py` → `CHECK`).
- Omuz ölçümü uygulamadaki gibi omuz–ayak bileği mesafesine bakar; ayak bilekleri görünmüyorsa yalnızca baş ölçülür.

Tema cihaz ayarına uyar; menüdeki düğmeyle açık ya da koyu seçilebilir (`assets/js/site.js`, seçim tarayıcıda saklanır).

Yazı tipi (Inter) ve three.js siteye gömülüdür; ziyaretçinin bilgisi üçüncü taraf bir sunucuya gitmez.

## Lisanslar

Koç karakterleri Microsoft Rocketbox (MIT, © 2020 Microsoft), three.js (MIT), MediaPipe Tasks Vision ve Pose Landmarker modeli (Apache 2.0), Inter (SIL OFL 1.1).
