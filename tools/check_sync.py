"""Offline guardrails for the paired Markdown/HTML content. See CONTRIBUTING.md."""
import re
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from unittest.mock import patch

from markdown_it import MarkdownIt
import build_pages

ROOT = Path(build_pages.ROOT)
# Exact editorial pairs, not a global URL comparison that can hide section drift.
PAIRS = {
    'story': 'stories/from-pass-to-position.md',
    'rescue': 'explore/real-world-robotics.md',
    'care': 'explore/healthcare-and-daily-life.md',
    'frontiers': 'explore/new-frontiers.md',
    'industry': 'explore/factories-and-construction.md',
    'farm': 'explore/farms-and-food.md',
    'throw': 'explore/throwing-robots.md',
    'watch': 'explore/listen-and-watch.md',
    'nature': 'explore/nature-and-curiosity.md',
    'future': 'discuss/questions-and-shared-standards.md',
    'events': 'events/README.md',
    'sources': 'SOURCES.md',
}


class Links(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if tag == 'a' and key == 'href' and value and value.startswith(('https://', 'http://')):
                self.links.add(value)


def markdown_links(text):
    # Rendering handles inline/reference links, HTML, escapes and parentheses.
    # HTMLParser normalizes entities; query strings/fragments remain significant.
    return Links(MarkdownIt('commonmark').render(text)).links


def check_parity(root=ROOT):
    source = (root / 'src/guide.html').read_text(encoding='utf-8')
    sections = dict(re.findall(r'(?s)<section id="([^"]+)">(.*?)</section>', source))
    errors = []
    expected = {page[0] for page in build_pages.PAGES}
    if expected != set(PAIRS):
        errors.append('Update PAIRS for the section pages in build_pages.PAGES')
    for section, filename in PAIRS.items():
        if section not in sections:
            errors.append(f'Missing source section: {section}')
            continue
        web = Links(sections[section]).links
        markdown = markdown_links((root / filename).read_text(encoding='utf-8'))
        for url in sorted(web - markdown):
            errors.append(f'{filename}: missing link from HTML #{section}: {url}')
        for url in sorted(markdown - web):
            errors.append(f'src/guide.html #{section}: missing link from {filename}: {url}')
    # README is a broader landing page, not a verbatim copy. Require every
    # visual-guide source there, without treating its other links as drift.
    readme = (root / 'README.md').read_text(encoding='utf-8')
    for url in sorted(Links(sections.get('guide', '')).links - markdown_links(readme)):
        errors.append(f'README.md: missing visual-guide source: {url}')
    watch = sections.get('watch', '')
    guests = len(re.findall(r'class="guest-ribbon"', watch))
    words = {word: number for number, word in enumerate(
        ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'])}
    for label, text in [('README.md', readme), ('HTML #watch', watch),
                        ('explore/listen-and-watch.md', (root / PAIRS['watch']).read_text(encoding='utf-8'))]:
        matches = re.findall(r'\b(\w+) (?:conversations with Lex Fridman|Lex Fridman conversations)\b', text, re.I)
        if not matches:
            errors.append(f'{label}: expected a Lex Fridman conversation count')
        for count in matches:
            value = int(count) if count.isdigit() else words.get(count.lower())
            if value != guests:
                errors.append(f'{label}: count {count!r} does not match {guests} guest ribbons')
    return errors


def check_freshness(root=ROOT):
    # Generate into a temporary directory, never rewriting a contributor's files.
    outputs = {}
    def read(path):
        return (root / path).read_text(encoding='utf-8').replace('\r\n', '\n')
    with tempfile.TemporaryDirectory() as destination:
        def write(path, text):
            target = Path(destination) / path
            target.write_text(text, encoding='utf-8', newline='\n')
            outputs[path] = target.read_bytes()
        # CI always checks the committed editorial date, not a local override.
        with patch.object(build_pages, 'read', read), patch.object(build_pages, 'write', write), patch.dict(build_pages.os.environ, {'SITE_DATE': read('src/site-date.txt').strip()}):
            build_pages.main()
    return [f'{path}: stale or missing; run python tools/build_pages.py'
            for path, expected in outputs.items()
            if not (root / path).exists() or (root / path).read_bytes() != expected]


def main():
    errors = check_parity() + check_freshness()
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print('Paired links, Lex counts and generated pages match.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
