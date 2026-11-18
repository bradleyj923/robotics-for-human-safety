"""Seed faults in isolated copies to prove the guardrails reject them."""
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import check_sync


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'repo'
        shutil.copytree(check_sync.ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__', '.venv'))

    def change(self, filename, old, new):
        path = self.root / filename
        text = path.read_text(encoding='utf-8')
        self.assertIn(old, text)
        path.write_text(text.replace(old, new), encoding='utf-8')

    def test_baseline(self):
        self.assertEqual(check_sync.check_parity(self.root), [])
        self.assertEqual(check_sync.check_freshness(self.root), [])

    def test_stale_generated_page(self):
        self.change('index.html', '<h1>', '<h1>stale ')
        self.assertTrue(any('index.html: stale' in error for error in check_sync.check_freshness(self.root)))

    def test_missing_link_in_one_pair(self):
        path = self.root / check_sync.PAIRS['throw']
        text = path.read_text(encoding='utf-8')
        link = next(iter(check_sync.markdown_links(text)))
        path.write_text(text.replace(link, 'https://example.org/seeded-fault'), encoding='utf-8')
        errors = check_sync.check_parity(self.root)
        self.assertTrue(any('explore/throwing-robots.md: missing' in error for error in errors))
        self.assertTrue(any('HTML' not in error and 'seeded-fault' in error for error in errors))

    def test_wrong_readme_count(self):
        self.change('README.md', 'Six conversations with Lex Fridman', 'Four conversations with Lex Fridman')
        self.assertTrue(any('README.md: count' in error for error in check_sync.check_parity(self.root)))

    def test_missing_home_guide_source(self):
        self.change('README.md', 'https://news.ki.se/drones-enabled-the-use-of-defibrillators-before-ambulance-arrival', 'https://example.org/replaced')
        self.assertTrue(any('missing visual-guide source' in error for error in check_sync.check_parity(self.root)))

    def test_date_does_not_follow_clock_or_local_override(self):
        class FutureDate(check_sync.build_pages.datetime.date):
            @classmethod
            def today(cls):
                return cls(2040, 1, 1)
        with patch.object(check_sync.build_pages.datetime, 'date', FutureDate), patch.dict(os.environ, {'SITE_DATE': '2039-12-01'}):
            self.assertEqual(check_sync.check_freshness(self.root), [])

    def test_markdown_entities_references_and_parentheses(self):
        text = '''[inline](https://example.org/wiki/Thing_(test)?a=1&b=2)
[reference][source]

[source]: https://example.org/reference "Title"
<https://example.org/auto>
<a href="https://example.org/html?a=1&amp;b=2">HTML</a>
`[not a link](https://example.org/code)`
'''
        self.assertEqual(check_sync.markdown_links(text), {
            'https://example.org/wiki/Thing_(test)?a=1&b=2',
            'https://example.org/reference', 'https://example.org/auto',
            'https://example.org/html?a=1&b=2',
        })


if __name__ == '__main__':
    unittest.main()
