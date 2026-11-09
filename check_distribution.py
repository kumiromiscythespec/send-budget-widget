"""Static content contract only: no network, browser, accounts or production writes."""
from html.parser import HTMLParser
from html import unescape
from pathlib import Path
from urllib.parse import urlsplit, parse_qs
import json
import re

ROOT = Path(__file__).resolve().parent
ORIGIN = 'https://send-budget-1109.crisp-llama-2628.chatgpt.site'

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

def parsed(text):
    page = Page()
    page.feed(text)
    return page.tags

def frame_contract(tags):
    frames = [attrs for tag, attrs in tags if tag == 'iframe']
    assert len(frames) == 1
    frame = frames[0]
    assert frame['src'] == ORIGIN + '/embed/remaining-sends.html'
    assert frame['title'] == 'Remaining-send balance calculator by Send Budget'
    assert frame['sandbox'].split() == ['allow-scripts']
    assert frame['loading'] == 'lazy'
    assert frame['referrerpolicy'] == 'no-referrer'
    assert 'scrolling' not in frame and not frame.get('srcdoc')

def full_link_contract(tags):
    links = [attrs for tag, attrs in tags if tag == 'a' and 'utm_source=' in attrs.get('href', '')]
    assert len(links) == 1
    link = links[0]
    url = urlsplit(link['href'])
    assert url.scheme + '://' + url.netloc == ORIGIN
    assert url.path == '/capacity.html' and url.fragment == 'remaining-send-balance'
    assert parse_qs(url.query) == {'utm_source': ['github'], 'utm_medium': ['referral']}
    assert 'noreferrer' in link.get('rel', '').split()
    assert '&amp;' not in link['href']

html = (ROOT / 'index.html').read_text(encoding='utf-8')
snippet = (ROOT / 'copied-snippet.txt').read_text(encoding='utf-8')
readme = (ROOT / 'README.md').read_text(encoding='utf-8')
for source in (html, snippet):
    tags = parsed(source)
    frame_contract(tags)
    full_link_contract(tags)
    assert not any(tag in ('script', 'form', 'input') for tag, attrs in tags)
    assert not any(key.startswith('on') or key.startswith('data-affiliate') for tag, attrs in tags for key in attrs)
    assert not re.search(r'(metrics\.js|link-config|systeme\.io|try\.carrd|document\.cookie|localStorage|sessionStorage)', source)
    frame_position = next(i for i, (tag, attrs) in enumerate(tags) if tag == 'iframe')
    link_position = next(i for i, (tag, attrs) in enumerate(tags) if tag == 'a' and 'utm_source=' in attrs.get('href', ''))
    assert frame_position < link_position
displayed = re.search(r'<details class="embed-code">([\s\S]*?)</details>', html)
assert displayed and '<summary>View the embed code</summary>' in displayed.group(1)
code = re.search(r'<pre\b[^>]*><code>([\s\S]*?)</code></pre>', displayed.group(1))
assert code and unescape(code.group(1)) == snippet
assert not any(tag == 'iframe' for tag, attrs in parsed(displayed.group(1)))
assert html.index('</details>') < html.index('<section class="demo"')
assert 'overflow-x:auto;white-space:pre' in html and 'max-width:100%' in html
assert snippet.strip() in readme
assert '<iframe' not in readme.split('```html')[0]
assert html.count('<h1>') == 1
assert 'width:100%;height:1000px;border:0' in snippet
assert '.demo iframe{display:block;width:100%;height:1000px;border:0}' in html
assert 'overflow:hidden' not in html and 'overflow: hidden' not in html
assert '<meta name="viewport" content="width=device-width,initial-scale=1">' in html
assert 'operator-owned' in readme and 'not an independent review' in readme
assert 'does not contain an offline calculator' in readme
assert 'hosting/security' in readme and 'aggregate counts' in readme
assert not re.search(r'(?i)(MIT License|open[- ]source|Copyright \(c\)|mailto:)', readme + html)
assert sorted(p.name for p in ROOT.iterdir() if p.is_file()) == ['.nojekyll', 'README.md', 'check_distribution.py', 'copied-snippet.txt', 'index.html', 'sitemap.xml']
assert 'https://kumiromiscythespec.github.io/send-budget-widget/' in html and 'https://kumiromiscythespec.github.io/send-budget-widget/' in readme
print(json.dumps({'result': 'PASS', 'files': 6, 'scope': 'static HTML/snippet content only; no browser, network, adoption, traffic or revenue verification'}))
