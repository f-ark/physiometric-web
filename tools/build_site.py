#!/usr/bin/env python3
"""PosMetric sitesinin sayfalarını üretir: dört dil x beş sayfa, 404, site haritası.

Kullanım: python3 tools/build_site.py   (bağımlılık yok, Python 3.9+)
Metinler tools/content.py içindedir. Üretilen .html dosyaları elle düzenlenmez;
değişiklik content.py'de yapılıp betik yeniden çalıştırılır.
"""
from __future__ import annotations

import json
import pathlib
from html import escape

from content import LANGS, UI, HOME, LEGAL, CHECK

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://physiometric.app"
PAGES = ["index", "privacy", "terms", "delete-account", "developer"]
PLAY = "https://play.google.com/store/apps/details?id=com.fark.physiometric"


def url(lang: str, page: str) -> str:
    base = "/" if lang == "tr" else f"/{lang}/"
    return base if page == "index" else f"{base}{page}.html"


def head(lang: str, page: str, title: str, desc: str, extra: str = "") -> str:
    alts = "\n".join(
        f'  <link rel="alternate" hreflang="{l}" href="{SITE}{url(l, page)}">' for l in LANGS
    )
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(desc)}">
  <link rel="canonical" href="{SITE}{url(lang, page)}">
{alts}
  <link rel="alternate" hreflang="x-default" href="{SITE}{url('en', page)}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="PosMetric">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(desc)}">
  <meta property="og:url" content="{SITE}{url(lang, page)}">
  <meta property="og:image" content="{SITE}/assets/img/og-{lang}.jpg">
  <meta property="og:locale" content="{UI[lang]['locale']}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#F4F7FB" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#12121F" media="(prefers-color-scheme: dark)">
  <link rel="icon" type="image/png" href="/assets/app_icon.png">
  <link rel="apple-touch-icon" href="/assets/app_icon.png">
  <link rel="preload" href="/assets/fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
  <script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
  <link rel="stylesheet" href="/assets/css/site.css">
  <script src="/assets/js/site.js" defer></script>
{extra}</head>"""


def topbar(lang: str, page: str) -> str:
    u = UI[lang]
    home = url(lang, "index")
    menu = ""
    if page == "index":
        menu = "".join(f'<a href="#{k}">{escape(v)}</a>' for k, v in u["nav"])
    else:
        menu = f'<a href="{home}">{escape(u["home"])}</a>'
    target = "index" if page == "404" else page
    langs = "".join(
        f'<a href="{url(l, target)}" hreflang="{l}" lang="{l}"'
        + (' aria-current="page"' if l == lang else "")
        + f' title="{escape(UI[l]["lang_name"])}">{l.upper()}</a>'
        for l in LANGS
    )
    return f"""<body>
<a class="skip" href="#main">{escape(u['skip'])}</a>
<header class="top">
  <div class="wrap">
    <a class="brand" href="{home}"><img src="/assets/app_icon.png" alt="" width="32" height="32">PosMetric</a>
    <nav class="menu" aria-label="{escape(u['nav_label'])}">{menu}</nav>
    <nav class="langs" aria-label="{escape(u['lang_label'])}">{langs}</nav>
    <button class="theme-btn" type="button" data-theme-toggle aria-label="{escape(u['theme'])}" title="{escape(u['theme'])}">
      <svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
      <svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
    </button>
  </div>
</header>"""


def stores(lang: str) -> str:
    u = UI[lang]
    return f"""<div class="stores">
        <a class="store play" href="{PLAY}&amp;hl={u['play_hl']}"><img src="/assets/play_store_logo.svg" alt="" width="22" height="22"><span><small>{escape(u['play_small'])}</small>Google Play</span></a>
        <span class="store apple" aria-disabled="true"><img src="/assets/apple_logo.svg" alt="" width="22" height="22"><span><small>{escape(u['soon'])}</small>App Store</span></span>
      </div>"""


def footer(lang: str) -> str:
    u = UI[lang]
    links = "".join(
        f'<a href="{url(lang, p)}">{escape(u["links"][p])}</a>' for p in ["privacy", "terms", "developer", "delete-account"]
    )
    return f"""<footer class="foot">
  <div class="wrap">
    <div><a class="brand" href="{url(lang, 'index')}"><img src="/assets/app_icon.png" alt="" width="32" height="32">PosMetric</a>
      <p style="margin-top:10px">{escape(u['tagline'])}</p></div>
    <nav aria-label="{escape(u['footer_label'])}">{links}<a href="mailto:info@physiometric.app">{escape(u['contact'])}</a></nav>
    <p class="disc">{escape(u['disclaimer'])} · © 2026 FArk Studio</p>
  </div>
</footer>
</body>
</html>
"""


def rings(states: list[str], labels: list[str], cls: str = "") -> str:
    items = "".join(
        f'<span class="ring {s}"><i></i>{escape(d)}</span>' for s, d in zip(states, labels)
    )
    return f'<div class="rings {cls}" aria-hidden="true">{items}</div>'


def hero_demo(lang: str) -> str:
    """Karşılamadaki ölçüm canlandırması: önden ve yandan çekim, ardından sonuç kartı.

    Noktalar örnek fotoğraflarda poz modelinin (MediaPipe Pose Landmarker lite) gerçek çıktısıdır;
    sonuçlar uygulamanın formülleriyle hesaplandı:
    - Önden: baş eğikliği 0,6° (eşik 3°), omuz yükseklik farkı %1,1 (eşik %2) → bulgu yok.
      Güçlü yan, uygulamadaki bölge sırasıyla omuz.
    - Yandan (çekül hattı): kulak, beş noktanın ortalamasından gövde boyunun %14'ü kadar önde
      (eşik %1,8) → İleri baş duruşu.
    Fotoğraflar değişirse model yeniden çalıştırılıp konumlar güncellenir."""
    c, h = CHECK[lang], HOME[lang]
    # 340x820 kırpılmış fotoğraflarda piksel konumları (kırpma: önden x 97, yandan x 80, ikisinde y 80)
    f = {"nose": (165.6, 127.4), "le": (191.7, 121.3), "re": (142, 121.8), "ls": (242.4, 215.4), "rs": (98.3, 223.1),
         "lel": (263.7, 333.8), "rel": (72.5, 335.2), "lw": (267.2, 440.1), "rw": (67.4, 438),
         "lh": (212.1, 424.6), "rh": (128.5, 427.2), "lk": (210.5, 593.6), "rk": (126.2, 590.3),
         "la": (215, 752.5), "ra": (125.1, 754.2)}
    fb = [("ls", "rs"), ("ls", "lel"), ("lel", "lw"), ("rs", "rel"), ("rel", "rw"), ("ls", "lh"), ("rs", "rh"),
          ("lh", "rh"), ("lh", "lk"), ("lk", "la"), ("rh", "rk"), ("rk", "ra")]
    sd = {"ear": (151, 122.3), "sh": (186.7, 202.8), "hip": (187.5, 429.5), "knee": (189.6, 588.9), "ank": (203.9, 754.6)}
    ref = 183.7  # çekül hattı: beş noktanın x ortalaması

    def line(p, q, cls=""):
        return f'<line{cls} x1="{p[0]}" y1="{p[1]}" x2="{q[0]}" y2="{q[1]}"/>'

    def ext(p, q, k=0.45):
        dx, dy = q[0] - p[0], q[1] - p[1]
        return (round(p[0] - dx * k, 1), round(p[1] - dy * k, 1)), (round(q[0] + dx * k, 1), round(q[1] + dy * k, 1))

    def dots(pts):
        return "".join(f'<circle cx="{x}" cy="{y}" r="6" style="--d:{i * 0.05:.2f}s"/>' for i, (x, y) in enumerate(pts))

    mx = round((f["la"][0] + f["ra"][0]) / 2, 1)
    front = (
        f'<g class="bones">{"".join(line(f[a], f[b]) for a, b in fb)}</g>'
        f'<line class="mid" x1="{mx}" y1="40" x2="{mx}" y2="780"/>'
        f'{line(*ext(f["re"], f["le"]), cls=" class=ok")}{line(*ext(f["rs"], f["ls"], 0.25), cls=" class=ok")}'
        f'<g class="dots">{dots(f.values())}</g>'
    )
    chain = ["ear", "sh", "hip", "knee", "ank"]
    side = (
        f'<g class="bones">{"".join(line(sd[a], sd[b]) for a, b in zip(chain, chain[1:]))}</g>'
        f'<line class="mid" x1="{ref}" y1="40" x2="{ref}" y2="780"/>'
        f'<line class="seen" x1="{ref}" y1="{sd["ear"][1]}" x2="{sd["ear"][0]}" y2="{sd["ear"][1]}"/>'
        f'<g class="dots">{dots(sd.values())}</g>'
        f'<circle class="seen-dot" cx="{sd["ear"][0]}" cy="{sd["ear"][1]}" r="10"/>'
    )

    def panel(cls, img, label, overlay):
        return f"""<div class="hd-panel {cls}">
          <img src="/assets/img/{img}" alt="" width="340" height="820"{' fetchpriority="high"' if cls == "front" else ' loading="eager"'}>
          <svg viewBox="0 0 340 820" preserveAspectRatio="xMidYMid slice"><line class="scan" x1="0" y1="0" x2="340" y2="0"/>{overlay}</svg>
          <span class="tag">{escape(label)}</span>
          <span class="pill hold">{escape(c['live']['stabilizing'])}</span>
          <span class="pill ok">{escape(c['live']['capturing_photo'])}</span>
          <i class="flash"></i>
        </div>"""

    return f"""<div class="hero-side"><figure class="hero-demo" aria-hidden="true">
        {panel("front", "hero-front.webp", c['front'], front)}
        {panel("side", "hero-side.webp", c['side'], side)}
        <div class="res-card">
          <small>{escape(c['res_title'])}</small>
          <div class="r"><span class="t">{escape(c['tag1'])}</span><b>{escape(c['name_fwd'])}</b><p>{escape(c['fwd_text'])}</p></div>
          <div class="r"><span class="t ok">{escape(c['strong_title'])}</span><p><span class="ok-i">✓</span>{escape(c['sh_strong'])}</p></div>
        </div>
      </figure>
      <p class="demo-cap">{escape(h['demo_caption'])}</p></div>"""


def home(lang: str) -> str:
    u, h = UI[lang], HOME[lang]
    ld = {
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": "PosMetric",
        "operatingSystem": "Android",
        "applicationCategory": "SportsApplication",
        "description": h["desc"],
        "inLanguage": list(LANGS),
        "url": SITE + url(lang, "index"),
        "downloadUrl": PLAY,
        "image": SITE + "/assets/app_icon.png",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "author": {"@type": "Organization", "name": "FArk Studio", "url": SITE, "email": "info@physiometric.app"},
    }
    extra = (
        '  <script type="importmap">{"imports":{"three":"/assets/vendor/three/three.module.min.js"}}</script>\n'
        '  <script type="module" src="/assets/js/coach.js"></script>\n'
        '  <script type="module" src="/assets/js/check.js"></script>\n'
        f'  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'
    )
    steps = "".join(
        f'<article class="card step"><span class="n">{i}</span><h3>{escape(t)}</h3><p>{escape(p)}</p></article>'
        for i, (t, p) in enumerate(h["steps"], 1)
    )
    f = h["finding"]
    week_list = "".join(f"<li>{x}</li>" for x in h["week_points"])
    packs = "".join(
        f'<div class="pack{" prio" if i == 0 else ""}"><img class="dot" src="/assets/img/paket/paket_{pid}_elif.webp" data-pack="{pid}" alt="" width="64" height="64" loading="lazy">'
        f'<span>{escape(name)}<small>{escape(h["pack_meta"])}</small></span>'
        + (f'<span class="prio-badge">{escape(h["priority"])}</span>' if i == 0 else "")
        + "</div>"
        for i, (pid, name) in enumerate(h["packs"])
    )
    regions = "".join(f'<span class="chip">{escape(r)}</span>' for r in h["regions"])
    fem, mal = h["coach_names"]
    moves = "".join(
        f'<button class="btn" type="button" data-move="{m}" data-guide-text="{escape(g)}" data-company-text="{escape(c)}" aria-pressed="false">{escape(n)}</button>'
        for m, n, g, c in h["moves"]
    )
    free = "".join(f"<li>{escape(x)}</li>" for x in h["free"])
    pro = "".join(f"<li>{escape(x)}</li>" for x in h["pro"])
    priv = "".join(f"<li>{x}</li>" for x in h["privacy_points"])
    faq = "".join(
        f"<details><summary>{escape(q)}</summary><p>{a}</p></details>" for q, a in h["faq"]
    )
    days = u["days"]
    return (
        head(lang, "index", h["title"], h["desc"], extra)
        + topbar(lang, "index")
        + f"""
<main id="main">
  <section class="hero stage-dark">
    <div class="wrap">
      <div>
        <span class="eyebrow">{escape(h['eyebrow'])}</span>
        <h1>{h['h1']}</h1>
        <p class="lead">{escape(h['lead'])}</p>
        <div class="hero-cta">
          <a class="btn primary big" href="#try">📷 {escape(h['try_btn'])}</a>
          <a class="store play" href="{PLAY}&amp;hl={u['play_hl']}"><img src="/assets/play_store_logo.svg" alt="" width="22" height="22"><span><small>{escape(u['play_small'])}</small>Google Play</span></a>
        </div>
        <p class="fine">{escape(h['try_hint'])}</p>
      </div>
      {hero_demo(lang)}
    </div>
  </section>

  <section id="try" class="check" data-check data-t="{check_data(lang)}">
    <div class="wrap">
      <div class="head center"><h2>{escape(h['try_title'])}</h2><p>{escape(h['try_sub'])}</p></div>
      {check_core(lang)}
    </div>
  </section>

  <section id="coach" class="stage-dark coach-sec" data-coach data-loading="{escape(h['loading'])}" data-error="{escape(h['load_error'])}">
    <div class="wrap">
      <div class="head center"><h2>{escape(h['coach_title'])}</h2><p>{escape(h['coach_sub'])}</p></div>
      <div class="coach-box">
        <div class="viewer">
          <img class="poster" src="/assets/img/coach-elif-idle.webp" alt="{escape(fem)}" width="261" height="900" loading="lazy">
          <p class="bubble" aria-live="polite"></p>
          <p class="status" aria-live="polite"></p>
        </div>
        <div class="controls">
          <div><h3>{escape(h['pick_coach'])}</h3><div class="row">
            <button class="btn" type="button" data-pick="elif" aria-pressed="true">{escape(fem)}</button>
            <button class="btn" type="button" data-pick="asim" aria-pressed="false">{escape(mal)}</button></div></div>
          <div><button class="btn primary" type="button" data-live>▶ {escape(h['live'])}</button></div>
          <div><h3>{escape(h['try_moves'])}</h3><div class="row">{moves}</div></div>
          <div><h3>{escape(h['listen'])}</h3><div class="row">
            <button class="btn" type="button" data-guide>🧭 {escape(h['guide'])}</button>
            <button class="btn" type="button" data-company>💬 {escape(h['company'])}</button></div></div>
          <p class="note">{escape(h['coach_note'])}</p>
        </div>
      </div>
    </div>
  </section>

  <section id="how">
    <div class="wrap">
      <div class="head center"><h2>{escape(h['how_title'])}</h2><p>{escape(h['how_sub'])}</p></div>
      <div class="grid3">{steps}</div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap grid2">
      <div class="head" style="margin:0"><h2>{escape(h['result_title'])}</h2><p>{escape(h['result_sub'])}</p></div>
      <article class="card finding">
        <span class="tag">{escape(f['tag'])}</span>
        <h3>{escape(f['name'])}</h3>
        <div class="row"><span class="ico" aria-hidden="true">👁</span><span>{escape(f['obs'])}</span></div>
        <div class="row"><span class="ico" aria-hidden="true">🕒</span><span>{escape(f['daily'])}</span></div>
        <div class="row"><span class="ico" aria-hidden="true">🧭</span><span>{escape(f['plan'])}</span></div>
        <p class="strong"><b>{escape(f['strong_label'])}</b>{escape(f['strong'])}</p>
      </article>
    </div>
  </section>

  <section id="week">
    <div class="wrap grid2">
      <div>
        <div class="head" style="margin-bottom:24px"><h2>{escape(h['week_title'])}</h2><p>{escape(h['week_sub'])}</p></div>
        <ul class="list">{week_list}</ul>
      </div>
      <div class="card">
        <p style="font-weight:800;margin-bottom:14px">{escape(h['week_example'])}</p>
        {rings(['full','gold','full','rest','full','gold','rest'],days,'big-rings')}
        <div class="legend"><span class="full"><i></i>{escape(h['legend'][0])}</span><span class="gold"><i></i>{escape(h['legend'][1])}</span><span class="rest"><i></i>{escape(h['legend'][2])}</span></div>
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap">
      <div class="head center"><h2>{escape(h['packs_title'])}</h2><p>{escape(h['packs_sub'])}</p></div>
      <div class="packs">{packs}</div>
    </div>
  </section>

  <section>
    <div class="wrap grid2">
      <div class="head" style="margin:0"><h2>{escape(h['sens_title'])}</h2><p>{escape(h['sens_sub'])}</p></div>
      <div class="card">
        <div class="chips" style="margin-bottom:18px">{regions}</div>
        <div class="chips"><span class="chip">🌿 {escape(h['gentle'])}</span><span class="chip">⏸ {escape(h['rest'])}</span></div>
      </div>
    </div>
  </section>

  <section id="pricing" class="alt">
    <div class="wrap">
      <div class="head center"><h2>{escape(h['price_title'])}</h2><p>{escape(h['price_sub'])}</p></div>
      <div class="plans">
        <article class="card plan"><h3>{escape(h['free_name'])}</h3><p class="sub">{escape(h['free_sub'])}</p><ul class="list">{free}</ul></article>
        <article class="card plan pro"><span class="badge">PRO</span><h3>PosMetric Pro</h3><p class="sub">{escape(h['pro_sub'])}</p><ul class="list">{pro}</ul></article>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap grid2">
      <div class="head" style="margin:0"><h2>{escape(h['priv_title'])}</h2><p>{escape(h['priv_sub'])}</p>
        <p style="margin-top:16px"><a href="{url(lang,'privacy')}" style="color:var(--primary);font-weight:700">{escape(h['priv_link'])} →</a></p></div>
      <ul class="list card">{priv}</ul>
    </div>
  </section>

  <section id="faq">
    <div class="wrap">
      <div class="head center"><h2>{escape(h['faq_title'])}</h2></div>
      <div class="faq">{faq}</div>
    </div>
  </section>

  <section class="alt cta-final">
    <div class="wrap">
      <div class="head center" style="margin-bottom:0"><h2>{escape(h['end_title'])}</h2><p>{escape(h['end_sub'])}</p></div>
      {stores(lang)}
    </div>
  </section>
</main>
"""
        + footer(lang)
    )


def doc(lang: str, page: str) -> str:
    d = LEGAL[lang][page]
    date = f'<p class="date">{escape(UI[lang]["updated"])}: {escape(d["date"])}</p>' if d.get("date") else ""
    return (
        head(lang, page, f'{d["title"]} — PosMetric', d["desc"])
        + topbar(lang, page)
        + f'\n<main id="main" class="doc">\n<h1>{escape(d["title"])}</h1>\n{date}\n{d["body"]}\n</main>\n'
        + footer(lang)
    )


def check_data(lang: str) -> str:
    """check.js'in okuduğu metinler (data-t)."""
    c = CHECK[lang]
    skip = {"title", "desc", "eyebrow", "h1", "lead", "privacy", "pick", "sound", "tips_title", "tips", "start",
            "cta_title", "app_title", "app_lead", "free_tag", "app_items"}
    return escape(json.dumps({k: v for k, v in c.items() if k not in skip}, ensure_ascii=False))


def check_core(lang: str) -> str:
    """Mini kontrolün kamera, ayarlar ve sonuç alanı; anasayfada ve /mini-check.html'de aynıdır."""
    c = CHECK[lang]
    fem, mal = HOME[lang]["coach_names"]
    tips = "".join(f"<li>{escape(t)}</li>" for t in c["tips"])
    items = "".join(
        f'<li><span class="ico">{i}</span><div><b>{escape(h)}</b>'
        + (f' <span class="free">{escape(c["free_tag"])}</span>' if free else "")
        + f'<p>{escape(d.format(fem=fem, mal=mal))}</p></div></li>'
        for i, h, d, free in c["app_items"]
    )
    return f"""<div class="check-box">
        <div class="cam">
          <video playsinline muted></video>
          <canvas></canvas>
          <p class="live-pill" aria-live="polite"></p>
          <div class="hold-bar" aria-hidden="true"><i></i></div>
          <div class="cam-actions">
            <button class="btn primary" type="button" data-start>📷 {escape(c['start'])}</button>
          </div>
          <p class="status" aria-live="polite"></p>
        </div>
        <div class="side">
          <h3>{escape(c['pick'])}</h3>
          <div class="row">
            <button class="btn" type="button" data-pick="elif" aria-pressed="true">{escape(fem)}</button>
            <button class="btn" type="button" data-pick="asim" aria-pressed="false">{escape(mal)}</button>
          </div>
          <label class="switch"><input type="checkbox" data-sound checked> <span>🔊 {escape(c['sound'])}</span></label>
          <h3>{escape(c['tips_title'])}</h3>
          <ul class="tips">{tips}</ul>
          <p class="callout key">🔒 {escape(c['privacy'])}</p>
        </div>
      </div>
      <div class="results" aria-live="polite" hidden>
        <div class="res-head">
          <div><h2>{escape(c['res_title'])}</h2><p class="date"></p></div>
          <button class="btn" type="button" data-again>↻ {escape(c['again'])}</button>
        </div>
        <div class="res-grid">
          <figure class="shot"><canvas></canvas><figcaption>{escape(c['front'])}</figcaption></figure>
          <div class="res-body"></div>
        </div>
        <div class="pitch card">
          <h2>{escape(c['app_title'])}</h2>
          <p>{escape(c['app_lead'])}</p>
          <ul class="app-list">{items}</ul>
          {stores(lang)}
          <p class="fine">{escape(HOME[lang]['fine'])}</p>
        </div>
      </div>"""


def check(lang: str) -> str:
    """Mini kontrolün tek başına sayfası: paylaşmak için. Anasayfadakinin aynısı; menüde ve site
    haritasında yok, arama motorlarına kapalı (aynı içerik anasayfada)."""
    c = CHECK[lang]
    return (
        head(lang, "mini-check", c["title"], c["desc"],
             '  <meta name="robots" content="noindex">\n'
             '  <script type="module" src="/assets/js/check.js"></script>\n')
        + topbar(lang, "mini-check")
        + f"""
<main id="main" class="check" data-check data-t="{check_data(lang)}">
  <section>
    <div class="wrap">
      <div class="head center">
        <span class="eyebrow">{escape(c['eyebrow'])}</span>
        <h1>{escape(c['h1'])}</h1>
        <p>{escape(c['lead'])}</p>
      </div>
      {check_core(lang)}
    </div>
  </section>
  <section class="alt cta-final" data-cta>
    <div class="wrap">
      <div class="head center" style="margin-bottom:0"><h2>{escape(c['cta_title'])}</h2><p>{escape(HOME[lang]['end_sub'])}</p></div>
      {stores(lang)}
    </div>
  </section>
</main>
"""
        + footer(lang)
    )


def not_found() -> str:
    blocks = "".join(
        f'<p lang="{l}">{escape(UI[l]["nf"])} <a href="{url(l, "index")}" style="color:var(--primary)">{escape(UI[l]["home"])}</a></p>'
        for l in LANGS
    )
    return (
        head("en", "index", "404 — PosMetric", "Page not found.").replace(
            f'<link rel="canonical" href="{SITE}/en/">', ""
        )
        + topbar("en", "404")
        + f'\n<main id="main" class="nf"><h1>404</h1>{blocks}</main>\n'
        + footer("en")
    )


def main() -> None:
    written = []
    for lang in LANGS:
        for page in PAGES:
            html = home(lang) if page == "index" else doc(lang, page)
            out = ROOT / (url(lang, page).lstrip("/") or "index.html")
            if out.name == "" or url(lang, page).endswith("/"):
                out = ROOT / url(lang, page).lstrip("/") / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(html, encoding="utf-8")
            written.append(out)
    for lang in LANGS:
        out = ROOT / url(lang, "mini-check").lstrip("/")
        out.write_text(check(lang), encoding="utf-8")
        written.append(out)
    (ROOT / "404.html").write_text(not_found(), encoding="utf-8")
    entries = []
    for page in PAGES:
        for lang in LANGS:
            alts = "".join(
                f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{url(l, page)}"/>' for l in LANGS
            )
            entries.append(f"  <url>\n    <loc>{SITE}{url(lang, page)}</loc>{alts}\n  </url>")
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(entries)
        + "\n</urlset>\n",
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print(f"{len(written)} sayfa, 404.html, sitemap.xml, robots.txt yazıldı")


if __name__ == "__main__":
    main()
