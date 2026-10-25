"""Paylaşım görsellerini (assets/img/og-{dil}.jpg, 1200×630) çizer.

Kullanım: python3 tools/og_gorselleri.py <koclar_grup.png>
Koç görseli uygulamanın mağaza görsellerindeki dört koç
(physio_metric/tool/store_listing/src/koclar_grup.png). Sayfa Chrome ile
ekran görüntüsüne çevrilir; metinler content.py'den gelir.
"""
import base64
import pathlib
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from content import HOME, LANGS, UI  # noqa: E402

KOK = pathlib.Path(__file__).resolve().parents[1]
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
DUGME = {'tr': 'Ücretsiz başla · Google Play', 'en': 'Start free · Google Play',
         'de': 'Kostenlos starten · Google Play', 'es': 'Empieza gratis · Google Play'}


def veri(yol, tur):
    return f'data:{tur};base64,' + base64.b64encode(pathlib.Path(yol).read_bytes()).decode()


def sayfa(dil, koclar):
    yazi = veri(KOK / 'assets/fonts/inter-latin-ext-wght-normal.woff2', 'font/woff2')
    yazi2 = veri(KOK / 'assets/fonts/inter-latin-wght-normal.woff2', 'font/woff2')
    ikon = veri(KOK / 'assets/app_icon.png', 'image/png')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Inter;src:url({yazi2}) format('woff2');font-weight:100 900}}
@font-face{{font-family:Inter;src:url({yazi}) format('woff2');font-weight:100 900;unicode-range:U+0100-024F,U+1E00-1EFF}}
html,body{{margin:0;width:1200px;height:630px;overflow:hidden}}
body{{font-family:Inter,sans-serif;color:#fff;position:relative;
background:radial-gradient(ellipse 620px 520px at 900px 210px,#5a1f3a 0%,rgba(90,31,58,0) 70%),
radial-gradient(ellipse 700px 420px at 80px 620px,#16384a 0%,rgba(22,56,74,0) 70%),#15141f}}
.sol{{position:absolute;left:72px;top:106px;width:580px}}
.marka{{display:flex;align-items:center;gap:16px;font-weight:700;font-size:30px}}
.marka img{{width:56px;height:56px;border-radius:13px;background:#fff}}
h1{{font-size:64px;line-height:1.08;letter-spacing:-2px;margin:28px 0 0;font-weight:800}}
h1 span{{background:linear-gradient(90deg,#E94560,#c58fb7 70%,#7ec8e3);-webkit-background-clip:text;color:transparent}}
p{{font-size:24px;line-height:1.5;color:#c9cad6;margin:26px 0 0;width:540px}}
.dugme{{display:inline-block;margin-top:30px;padding:14px 20px;border-radius:26px;border:1px solid rgba(255,255,255,.18);
background:rgba(255,255,255,.08);font-weight:700;font-size:19px}}
.koclar{{position:absolute;right:16px;bottom:0;height:490px}}
</style></head><body>
<div class="sol"><div class="marka"><img src="{ikon}">PosMetric</div>
<h1>{HOME[dil]['h1']}</h1><p>{UI[dil]['tagline']}</p><span class="dugme">{DUGME[dil]}</span></div>
<img class="koclar" src="{koclar}">
</body></html>"""


def main():
    koclar = veri(sys.argv[1], 'image/png')
    with tempfile.TemporaryDirectory() as tmp:
        for dil in LANGS:
            html = pathlib.Path(tmp) / f'og-{dil}.html'
            png = pathlib.Path(tmp) / f'og-{dil}.png'
            html.write_text(sayfa(dil, koclar), encoding='utf-8')
            subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                            '--window-size=1200,630', f'--screenshot={png}', html.as_uri()],
                           check=True, capture_output=True)
            subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '88', str(png),
                            '--out', str(KOK / f'assets/img/og-{dil}.jpg')], check=True, capture_output=True)
            print('og', dil)


if __name__ == '__main__':
    main()
