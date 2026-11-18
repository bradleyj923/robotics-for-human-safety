# Contributing

Small, well-sourced improvements are welcome. Open a pull request; do not edit the generated HTML by hand. This repository currently has two editorial representations, not a single-source publishing system.

## Where to edit

Update the Markdown page **and** the matching section in `src/guide.html` when changing shared content. Keep the existing visual layout.

| Markdown | HTML section ID |
|---|---|
| `stories/from-pass-to-position.md` | `story` |
| `explore/real-world-robotics.md` | `rescue` |
| `explore/healthcare-and-daily-life.md` | `care` |
| `explore/new-frontiers.md` | `frontiers` |
| `explore/factories-and-construction.md` | `industry` |
| `explore/farms-and-food.md` | `farm` |
| `explore/throwing-robots.md` | `throw` |
| `explore/listen-and-watch.md` | `watch` |
| `explore/nature-and-curiosity.md` | `nature` |
| `discuss/questions-and-shared-standards.md` | `future` |
| `events/README.md` | `events` |
| `SOURCES.md` | `sources` |

The README is a landing page rather than an exact copy. Review its summaries, counts and curator information alongside the homepage sections `start`, `guide` and `curator`. Keep the four visual-guide source links in the README. If a new section is added, update both `PAGES` in the builder and `PAIRS` in the sync checker.

Present sources with the title/link first and a brief explanation beneath it. Distinguish deployed tools, research and design questions. Use original sources, verify the final links, and avoid em dashes in new prose.

## Build and check

Python 3.10 or later is required. The builder uses the standard library; the checker uses a pinned CommonMark parser.

```sh
python -m venv .venv
# Windows: .venv\Scripts\activate
. .venv/bin/activate
python -m pip install -r tools/requirements-checks.txt
python tools/build_pages.py
python -m unittest discover -s tests -v
python tools/check_sync.py
```

Commit the source edits and regenerated pages together. `src/site-date.txt` is the editorial date in `YYYY-MM-DD` form. Update it for a substantive content revision, not merely because a build ran. `SITE_DATE=YYYY-MM-DD` can override it for a local preview; the checker always uses the committed date. The footer's separate “Sources checked” date must only change after an actual source review.

The checks run on pull requests, read repository contents only, and do not deploy. They check:

- Byte-for-byte freshness of the homepage, 12 section pages and sitemap, generated in a temporary directory.
- External hyperlink parity within each mapped section, including reference-style Markdown links and HTML entities. Query parameters and fragments remain significant.
- Presence of the visual-guide source links in the README.
- Lex Fridman conversation counts against the actual guest ribbons.
- Existing builder assertions for section mapping and fragment destinations.

These are modest guardrails, not proof that all prose matches or every external page works. They do not audit downloadable PDFs, compare all README prose, test external availability, or replace visual/accessibility review. Deliberately different content needs human review rather than a blanket URL-ignore list. Open final pages in a browser when changing presentation; check any changed external links manually.

## Before requesting review

- [ ] Updated both editorial versions where applicable.
- [ ] Checked names, dates, counts and source explanations.
- [ ] Rebuilt and ran the tests and sync check.
- [ ] Included generated changes and checked the final links.
- [ ] Described any intentional differences or remaining limitations.

GitHub Pages settings and publication are outside these checks. A pull request is not approval to merge or change deployment settings.
