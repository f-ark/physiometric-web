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

from content import LANGS, UI, HOME, LEGAL

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
  <link rel="stylesheet" href="/assets/css/site.css">
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
        f'  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'
    )
    steps = "".join(
        f'<article class="card step"><span class="n">{i}</span><h3>{escape(t)}</h3><p>{escape(p)}</p></article>'
        for i, (t, p) in enumerate(h["steps"], 1)
    )
    f = h["finding"]
    week_list = "".join(f"<li>{x}</li>" for x in h["week_points"])
    packs = "".join(
        f'<div class="pack{" prio" if i == 0 else ""}"><span class="dot" aria-hidden="true">{ico}</span>'
        f'<span>{escape(name)}<small>{escape(h["pack_meta"])}</small></span>'
        + (f'<span class="prio-badge">{escape(h["priority"])}</span>' if i == 0 else "")
        + "</div>"
        for i, (ico, name) in enumerate(h["packs"])
    )
    regions = "".join(f'<span class="chip">{escape(r)}</span>' for r in h["regions"])
    moves = "".join(
        f'<button class="btn" type="button" data-move="{m}" aria-pressed="false">{escape(n)}</button>'
        for m, n in h["moves"]
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
  <section class="hero">
    <div class="wrap">
      <div>
        <span class="eyebrow">{escape(h['eyebrow'])}</span>
        <h1>{h['h1']}</h1>
        <p class="lead">{escape(h['lead'])}</p>
        {stores(lang)}
        <p class="fine">{escape(h['fine'])}</p>
      </div>
      <div class="stage">
        <img class="c elif" src="/assets/img/coach-elif.webp" alt="Elif" width="313" height="900" fetchpriority="high">
        <img class="c asim" src="/assets/img/coach-asim.webp" alt="Asım" width="374" height="900">
        <p class="bubble">{escape(h['hello'])}</p>
        <div class="weekcard">{escape(h['week_card'])}{rings(['full','gold','full','rest','',''],days[:6])}</div>
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

  <section id="coach" class="alt" data-coach data-greeting="{escape(h['hello'])}" data-cheer="{escape(h['cheer'])}" data-loading="{escape(h['loading'])}" data-error="{escape(h['load_error'])}">
    <div class="wrap">
      <div class="head center"><h2>{escape(h['coach_title'])}</h2><p>{escape(h['coach_sub'])}</p></div>
      <div class="coach-box">
        <div class="viewer">
          <img class="poster" src="/assets/img/coach-elif.webp" alt="Elif" width="313" height="900" loading="lazy">
          <p class="bubble" aria-live="polite"></p>
          <p class="status" aria-live="polite"></p>
        </div>
        <div class="controls">
          <div><h3>{escape(h['pick_coach'])}</h3><div class="row">
            <button class="btn" type="button" data-pick="elif" aria-pressed="true">Elif</button>
            <button class="btn" type="button" data-pick="asim" aria-pressed="false">Asım</button></div></div>
          <div><button class="btn primary" type="button" data-live>▶ {escape(h['live'])}</button></div>
          <div><h3>{escape(h['try_moves'])}</h3><div class="row">{moves}</div></div>
          <p class="note">{escape(h['coach_note'])}</p>
        </div>
      </div>
    </div>
  </section>

  <section id="pricing">
    <div class="wrap">
      <div class="head center"><h2>{escape(h['price_title'])}</h2><p>{escape(h['price_sub'])}</p></div>
      <div class="plans">
        <article class="card plan"><h3>{escape(h['free_name'])}</h3><p class="sub">{escape(h['free_sub'])}</p><ul class="list">{free}</ul></article>
        <article class="card plan pro"><span class="badge">PRO</span><h3>PosMetric Pro</h3><p class="sub">{escape(h['pro_sub'])}</p><ul class="list">{pro}</ul></article>
      </div>
    </div>
  </section>

  <section class="alt">
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
