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

- `assets/models/elif.glb`, `asim.glb`: uygulamadaki koçlardan (`physio_metric/assets/3d_animations/koc_sports_*.glb`) web için küçültülmüş kopyalar. Dört hareket (shoulder elevation, neck lateral stretch, glute bridge, cat-cow) ve bekleme duruşu kaldı; yatak modelin içinde, sopa ve duvar çıkarıldı. Dokular 1024 px WebP, geometri ve animasyon meshopt ile sıkıştırıldı (gltf-transform). Hareket etmeyen kanallar yalnızca değerleri düğümün varsayılanına eşitse atıldı (sabit ama farklı değerler uygulamada anlam taşıyor).
- `assets/audio/{dil}/{elif|asim}/guide/`: rehberlik, uygulamanın `coaching` sesleri (hareketi yönlendiren cümle).
- `assets/audio/{dil}/{elif|asim}/company/`: eşlik, uygulamanın `coach` sesleri (selam, yarısı tamam, son üç, mola, kutlama).
- Dosya adlarındaki `elif` ve `asim` yalnızca kimliktir; ekranda görünen ad dile göre değişir (TR Elif/Asım, EN Emma/Jack, DE Anna/Max, ES Lucía/Carlos; `tools/content.py`).
- `assets/img/coach-*.webp`, `og-*.jpg`: modellerden çizilmiş görseller.

Yazı tipi (Inter) ve three.js siteye gömülüdür; ziyaretçinin bilgisi üçüncü taraf bir sunucuya gitmez.

## Lisanslar

Koç karakterleri Microsoft Rocketbox (MIT, © 2020 Microsoft), three.js (MIT), Inter (SIL OFL 1.1).
