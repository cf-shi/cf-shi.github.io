"""Check local HTML structure, resources and fragment links; no dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.stack, self.errors, self.links = [], [], []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.stack and self.stack[-1] in ('ul', 'ol') and tag != 'li':
            self.errors.append('Lists must contain li elements: ' + tag)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.errors.append('Duplicate id: ' + attrs['id'])
            self.ids.add(attrs['id'])
        if tag == 'img' and not attrs.get('alt'):
            self.errors.append('Image needs descriptive alt text')
        for key in ('src', 'href'):
            if key in attrs:
                self.links.append(attrs[key])
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            self.errors.append('Unbalanced closing tag: ' + tag)
        else:
            self.stack.pop()


pages = {}
for path in ROOT.rglob('*.html'):
    if any(part.startswith('.') or part == 'node_modules' for part in path.relative_to(ROOT).parts):
        continue
    page = Page(path)
    page.feed(path.read_text(encoding='utf-8'))
    page.close()
    if page.stack:
        page.errors.append('Unclosed tags: ' + ', '.join(page.stack))
    pages[path.resolve()] = page

errors = []
for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = ((ROOT / unquote(url.path).lstrip('/')) if url.path.startswith('/')
                  else (path.parent / unquote(url.path))) if url.path else path
        target = target.resolve()
        if target.is_dir():
            target = target / 'index.html'
        if not target.exists():
            page.errors.append('Missing local resource: ' + link)
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            page.errors.append('Missing anchor: ' + link)
    errors.extend(str(path.relative_to(ROOT)) + ': ' + error for error in page.errors)

if not pages:
    errors.append('No HTML pages found')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('PASS: {} HTML page(s); structure, local resources and anchors checked.'.format(len(pages)))
