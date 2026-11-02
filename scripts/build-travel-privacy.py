"""Build independently readable, static privacy policies for the 16 app locales.

Only the legacy root entry uses browser-language routing. Explicit locale pages
always retain the chosen language. No cookies, storage, analytics or remote code.
"""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'pocket-korean-travel' / 'privacy'
LANGUAGES = ['en', 'ja', 'zh-Hant', 'zh-Hans', 'es', 'pt-BR', 'fr', 'de',
             'tr', 'id', 'vi', 'th', 'hi', 'ne', 'km', 'bn']
DATE = '2026-11-02'
APP = 'Pocket Korean: Korea Travel'
CONTACT = 'davidleepub@gmail.com'
PUBLIC = 'https://minor-orbit.github.io/medical-chinese-legal/pocket-korean-travel/privacy/'

SOURCES = [
    ('Google privacy', 'https://policies.google.com/privacy'),
    ('Google Ads', 'https://policies.google.com/technologies/ads'),
    ('Google AdMob SDK', 'https://developers.google.com/admob/android/privacy/play-data-disclosure'),
    ('Unity privacy', 'https://unity.com/legal/privacy-policy'),
    ('Unity privacy choices', 'https://unity.com/legal/privacy-policy#privacy-rights'),
    ('Unity Ads SDK 4.21.0', 'https://docs.unity.com/en-us/ads-android/4.21.0/privacy/developer-consent/disclosures/google-data-safety'),
    ('GitHub Pages', 'https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement'),
]

CSS = '''
:root{color-scheme:light;--ink:#243c38;--link:#225e55;--paper:#fffcf5;--line:#d8dfda}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.8 system-ui,-apple-system,"Segoe UI",sans-serif;overflow-wrap:anywhere}
main{max-width:850px;margin:auto;padding:32px 22px 56px}h1{font-size:clamp(1.8rem,5vw,2.6rem);line-height:1.35;margin:24px 0 12px}h2{font-size:1.22rem;line-height:1.65;margin:0 0 10px}p{margin:0 0 15px}a{color:var(--link);text-underline-offset:3px}a:focus-visible{outline:3px solid #8056ad;outline-offset:3px}nav{border:1px solid var(--line);border-radius:16px;padding:14px 16px}nav strong{display:block}nav ul{display:flex;flex-wrap:wrap;gap:4px 14px;list-style:none;margin:8px 0 0;padding:0}nav a{display:inline-block;min-height:44px;padding:6px 0}nav [aria-current=page]{font-weight:700;text-decoration-thickness:3px}.meta{color:#475a56;font-size:.9rem;border-bottom:1px solid var(--line);padding-bottom:22px}.meta code{font-size:.85rem}section{padding-top:23px;border-bottom:1px solid var(--line);padding-bottom:8px}footer{margin-top:28px}footer ul{padding-left:22px}footer a{display:inline-block;padding:5px 0;min-height:40px}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
'''.strip()

ROUTER = '''// Browser language is used only at the old shared entry URL.
// An explicit /privacy/{locale}/ page is never redirected.
(function () {
  "use strict";
  const supported = ["en","ja","zh-Hant","zh-Hans","es","pt-BR","fr","de","tr","id","vi","th","hi","ne","km","bn"];
  function resolve(tag) {
    const parts = String(tag || "").replace(/_/g, "-").toLowerCase().split("-");
    const language = parts[0];
    const subtags = parts.slice(1);
    if (language === "zh") {
      if (subtags.includes("hant")) return "zh-Hant";
      if (subtags.includes("hans")) return "zh-Hans";
      return subtags.some(x => ["tw","hk","mo"].includes(x)) ? "zh-Hant" : "zh-Hans";
    }
    if (language === "pt") return "pt-BR";
    if (language === "in") return "id";
    return supported.includes(language) ? language : "en";
  }
  // Export only the pure function for deterministic local verification.
  if (typeof module !== "undefined" && module.exports) { module.exports = resolve; return; }
  if (typeof window === "undefined") return;
  const target = resolve((navigator.languages && navigator.languages[0]) || navigator.language);
  if (target !== "en") window.location.replace(new URL(target + "/", window.location.href).href);
})();
'''

def policies():
    combined = {}
    for path in sorted(BASE.glob('translations*.json')):
        value = json.loads(path.read_text(encoding='utf-8-sig'))
        assert not (combined.keys() & value.keys()), 'Duplicate locale'
        combined.update(value)
    assert set(combined) == set(LANGUAGES)
    for language, policy in combined.items():
        assert set(policy) == {'name', 'title', 'language', 'updated', 'contact', 'sections'}
        assert len(policy['sections']) == 12, language
        assert all(len(section) == 2 and all(isinstance(s, str) and s.strip() for s in section)
                   for section in policy['sections']), language
    return combined

def page(language, data, entry=False):
    p = data[language]
    prefix = './' if entry else '../'
    nav = '\n'.join(
        f'<li><a href="{prefix}{code}/" lang="{code}" hreflang="{code}"'
        + (' aria-current="page"' if code == language else '')
        + f'>{escape(data[code]["name"])}</a></li>' for code in LANGUAGES)
    sections = '\n'.join(f'<section id="section-{i}"><h2>{i}. {escape(title)}</h2><p>{escape(text)}</p></section>'
                         for i, (title, text) in enumerate(p['sections'], 1))
    alternate = '\n'.join(f'<link rel="alternate" hreflang="{code}" href="{PUBLIC}{code}/">' for code in LANGUAGES)
    source_links = '\n'.join(f'<li><a href="{escape(url, quote=True)}" rel="noreferrer">{escape(name)}</a></li>'
                             for name, url in SOURCES)
    script = '<script src="language.js" defer></script>' if entry else ''
    return f'''<!doctype html>
<html lang="{language}">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="referrer" content="no-referrer"><title>{escape(p['title'])} — {escape(APP)}</title>
<link rel="canonical" href="{PUBLIC}{language}/">{alternate}
<link rel="alternate" hreflang="x-default" href="{PUBLIC}"><style>{CSS}</style>{script}</head>
<body><main>
<nav aria-label="{escape(p['language'], quote=True)}"><strong>{escape(p['language'])}</strong><ul>{nav}</ul></nav>
<h1>{escape(p['title'])}</h1><p class="meta"><strong>{escape(APP)}</strong> · Minor Orbit<br>
<code>com.minororbit.koreatravel</code><br>{escape(p['updated'])}: <time datetime="{DATE}">{DATE}</time><br>
{escape(p['contact'])}: <a href="mailto:{CONTACT}">{CONTACT}</a></p>
{sections}
<footer><p>Google · Unity · GitHub</p><ul>{source_links}</ul>
<p>{escape(p['contact'])}: <a href="mailto:{CONTACT}">{CONTACT}</a></p></footer>
</main></body></html>
'''

if __name__ == '__main__':
    data = policies()
    for language in LANGUAGES:
        path = BASE / language / 'index.html'
        path.parent.mkdir(exist_ok=True)
        path.write_text(page(language, data), encoding='utf-8')
    (BASE / 'index.html').write_text(page('en', data, entry=True), encoding='utf-8')
    (BASE / 'language.js').write_text(ROUTER, encoding='utf-8')
    print('Built root + 16 independent localized policies, each with 12 sections.')
