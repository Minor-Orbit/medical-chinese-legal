"""Static structural and high-risk semantic checks, not native-speaker certification."""
import importlib.util
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('builder', ROOT/'scripts/build-travel-privacy.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)

class PolicyParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.language = None
        self.headings = 0
        self.links = []
        self.scripts = []
        self.text = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html': self.language = a.get('lang')
        if tag == 'h2': self.headings += 1
        if tag == 'a': self.links.append(a)
        if tag == 'script': self.scripts.append(a)
        assert tag not in {'iframe','form','input','img'}, tag
    def handle_data(self, data): self.text.append(data)

def check():
    data = b.policies()
    for code in b.LANGUAGES:
        path = b.BASE/code/'index.html'
        html = path.read_text(encoding='utf-8')
        assert html == b.page(code, data), f'Stale generated file {code}'
        p = PolicyParser();p.feed(html)
        assert p.language == code and p.headings == 12 and not p.scripts, code
        language_links = [a for a in p.links if 'hreflang' in a]
        assert {a['hreflang'] for a in language_links} == set(b.LANGUAGES), code
        assert len([a for a in language_links if a.get('aria-current') == 'page']) == 1
        for a in language_links:
            assert (path.parent/a['href']/'index.html').resolve().is_file(), (code,a)
        for expected in ['com.minororbit.koreatravel','Minor Orbit','2026-11-07',
                         'davidleepub@gmail.com','Unity','AdMob','GitHub','HANTEUM',
                         '4.21.0','25.5.0']:
            assert expected in ''.join(p.text), (code,expected)
        ad_text = data[code]['sections'][4][1]
        # Turkish places % before the number; French uses a separating space.
        for number in ['80','20']:
            assert re.search(r'(?:%'+number+r'|'+number+r'\s*%)',ad_text), (code,number)
        assert '\ufffd' not in html and 'chageun-' not in html
        assert b.BRANDS[code]['title'] in ''.join(p.text), code
        assert b.BRANDS[code]['previousLabel'] + ': HANTEUM: Travel Korean / Pocket Korean: Korea Travel' in ''.join(p.text), code
        assert all('Pocket Korean: Korea Travel' not in text for _,text in data[code]['sections']), code
        assert all(s not in html for s in ['TODO','TBD','Lorem ipsum','sk_live_'])
        # Data sent to each provider must not be described as entirely absent.
        assert len(data[code]['sections'][4][1]) > 350, code
        assert all(len(t) > 55 for _,t in data[code]['sections']), code
    root = (b.BASE/'index.html').read_text(encoding='utf-8')
    assert root == b.page('en',data,entry=True)
    p = PolicyParser();p.feed(root)
    assert p.language == 'en' and len(p.scripts) == 1
    assert p.scripts[0]['src'] == 'language.js'
    assert 'fetch(' not in b.ROUTER and 'localStorage' not in b.ROUTER and 'cookie' not in b.ROUTER
    print(json.dumps({'languages':b.LANGUAGES,'localizedPages':16,'sectionsPerPage':12,
                      'noJavascriptRequiredOnLocalePages':True,'status':'PASS'},ensure_ascii=False,indent=2))

if __name__ == '__main__': check()
