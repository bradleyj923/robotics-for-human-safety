"""Build the site's pages from the single source file.

    python tools/build_pages.py

Reads  src/guide.html  (the whole guide as one long page; edit this file)
Writes index.html, one page per section, and sitemap.xml at the repo root.

The generated pages are committed so GitHub Pages can serve them. Do not edit
them by hand: change src/guide.html (and the matching text file under
explore/, stories/ or discuss/), then run this script again.
"""
import html
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://bradleyj923.github.io/robotics-for-human-safety/"
SITE = "Robotics for Human Safety"

# section id -> (file name, navigation label, one-line description)
PAGES = [
    ("story", "why-it-matters.html", "Why it matters",
     "The personal story behind this collection and the question that started it."),
    ("rescue", "rescue-and-response.html", "Rescue & response",
     "Drone-delivered defibrillators, firefighting robots, indoor mapping and hazard sensing, with what is deployed and what is still research."),
    ("care", "health-and-daily-life.html", "Health & daily life",
     "Exoskeletons, walking assistance, and robots for independence and companionship, with the questions of consent they raise."),
    ("frontiers", "space-and-surgery.html", "Space & surgery",
     "Space robots, a rocket caught by its launch tower, robotic surgery at a distance and next-generation networks."),
    ("industry", "factories-and-construction.html", "Factories & construction",
     "Lights-out factories, what a machine can sense in the dark, what is easy and hard to automate, and autonomous equipment on building sites."),
    ("farm", "farms-and-food.html", "Farms & food",
     "Reading crop stress from a camera, robots already working in fields, dairy sensing and the hidden danger of manure storage."),
    ("throw", "throwing-robots.html", "Throwing robots",
     "Why throwing accurately is a serious robotics problem, the physics behind it, and where else the skill is needed."),
    ("watch", "listen-and-watch.html", "Listen & watch",
     "Conversations and videos worth your time, with what to look for in each."),
    ("nature", "learn-from-nature.html", "Learn from nature",
     "Biomimicry, the two ledgers, and why curiosity comes before credentials."),
    ("future", "build-a-better-future.html", "Build a better future",
     "Shared problems, shared standards, and a design challenge for a group."),
    ("events", "events.html", "Events", "Dates and events connected to this collection."),
    ("sources", "sources.html", "Sources", "Sources and the editorial approach behind every example."),
]
HOME_SECTIONS = ["start", "guide", "curator"]
HOME_DESC = ("A field guide for curious students and builders: rescue stories, real engineering "
             "examples and a challenge at the end of each. Curated by Bradley Shogren.")

EXTRA_CSS = (
    ".hub{display:grid;gap:10px;margin:18px 0 6px}"
    ".hub a{display:block;white-space:normal;font-size:1em;padding:14px 16px;border:1px solid #dbe5e9;"
    "border-radius:10px;text-decoration:none;background:#fff}"
    ".hub a b{display:block;color:#006f73;font-size:18px;margin-bottom:3px}"
    ".hub a span{display:block;color:#3d5463;font-size:15px;line-height:1.45}"
    ".pager{display:flex;flex-wrap:wrap;gap:10px 22px;justify-content:space-between;margin:26px 0 0;"
    "padding-top:14px;border-top:1px solid #dbe5e9;font-size:14px}"
    ".pager a{white-space:normal}"
    "nav a[aria-current=page]{text-decoration:underline;text-underline-offset:5px}"
    "header .eyebrow a{color:inherit;text-decoration:none;font-size:inherit;display:inline}"
    "header.sub{padding-top:30px;padding-bottom:26px}"
    "body{font-size:18px}@media(max-width:600px){body{font-size:18px;line-height:1.7}}"
)


def read(path):
    with io.open(os.path.join(ROOT, path), encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n")


def write(path, text):
    with io.open(os.path.join(ROOT, path), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main():
    src = read("src/guide.html")
    import datetime
    src = src.replace("{{UPDATED}}", datetime.date.today().strftime("%B %Y"))
    head_end = src.index("</head>")
    style = re.search(r"(?s)<style>(.*?)</style>", src[:head_end]).group(1)
    header = re.search(r"(?s)<header id=\"top\">.*?</header>", src).group(0)
    eyebrow = re.search(r"<div class=\"eyebrow\">(.*?)</div>", header).group(1)
    footer = re.search(r"(?s)<footer>.*?</footer>", src).group(0)
    intro = re.search(r"(?s)<div class=\"intro-grid\">.*?</div></div>", src)
    intro = intro.group(0) if intro else ""

    # sections, in document order
    sections = {}
    for m in re.finditer(r"(?s)<section id=\"([^\"]+)\">.*?</section>", src):
        sections[m.group(1)] = m.group(0)
    known = [p[0] for p in PAGES] + HOME_SECTIONS
    missing = [k for k in sections if k not in known]
    assert not missing, "section with no page assigned: %s" % missing
    assert all(k in sections for k in known), "a listed section is not in src/guide.html"

    # where every id lives
    where = {"top": None}
    for sid in HOME_SECTIONS:
        for i in re.findall(r"\bid=\"([^\"]+)\"", sections[sid]):
            where[i] = "index.html"
    for sid, fname, _, _ in PAGES:
        for i in re.findall(r"\bid=\"([^\"]+)\"", sections[sid]):
            where[i] = fname

    def relink(fragment, this_file):
        def fix(m):
            target = m.group(1)
            if target == "top":
                return 'href="#top"'
            page = where.get(target)
            assert page is not None, "link to unknown id #%s" % target
            if page == this_file:
                return 'href="#%s"' % target
            if page == "index.html":
                return 'href="./#%s"' % target
            # a link to a whole section goes to the top of its page
            if any(target == p[0] for p in PAGES):
                return 'href="%s"' % page
            return 'href="%s#%s"' % (page, target)
        return re.sub(r'href="#([^"]*)"', fix, fragment)

    def nav(this_file):
        out = ['<nav aria-label="Sections"><div class="inner">']
        cur = ' aria-current="page"' if this_file == "index.html" else ""
        out.append('<a href="./"%s>Start here</a>' % cur)
        for _, fname, label, _ in PAGES:
            cur = ' aria-current="page"' if this_file == fname else ""
            out.append('<a href="%s"%s>%s</a>' % (fname, cur, label))
        out.append("</div></nav>")
        return "".join(out)

    def page(this_file, title, desc, header_html, body):
        url = BASE + ("" if this_file == "index.html" else this_file)
        return (
            '<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            "<title>%s</title>"
            '<meta name="description" content="%s">'
            '<link rel="canonical" href="%s">'
            '<meta property="og:type" content="article"><meta property="og:site_name" content="%s">'
            '<meta property="og:title" content="%s"><meta property="og:description" content="%s">'
            '<meta property="og:url" content="%s">'
            "<style>%s%s</style></head><body>%s%s<main>%s</main>%s</body></html>\n"
        ) % (html.escape(title), html.escape(desc, quote=True), url, SITE, html.escape(title, quote=True),
             html.escape(desc, quote=True), url, style, EXTRA_CSS, header_html, nav(this_file), body, footer)

    # ---- home page
    hub = ['<section id="sections"><span class="tag">ALL SECTIONS</span><div style="height:18px"></div>'
           "<h2>Choose where to go</h2><div class=\"hub\">"]
    for _, fname, label, desc in PAGES:
        hub.append('<a href="%s"><b>%s</b><span>%s</span></a>' % (fname, label, html.escape(desc)))
    hub.append("</div></section>")
    note = ('<div class="note"><b>Each section has its own page.</b> Use the links above or the list below. '
            "Source links open in a new tab so you can explore without losing your place.</div>")
    redirect = {}
    for i, pg in where.items():
        if pg and pg != "index.html":
            redirect[i] = pg if any(i == p[0] for p in PAGES) else "%s#%s" % (pg, i)
    script = ("<script>(function(){var m=%s;function go(){var h=location.hash.slice(1);"
              "if(m[h]){location.replace(m[h]);}}go();window.addEventListener('hashchange',go);})();</script>") % (
        "{" + ",".join('"%s":"%s"' % kv for kv in sorted(redirect.items())) + "}")
    home_body = note + intro + relink(sections["start"], "index.html") + "".join(hub) + relink(sections["guide"], "index.html") + relink(sections["curator"], "index.html")
    home = page("index.html", SITE, HOME_DESC, header, home_body)
    home = home.replace("</body>", script + "</body>")
    write("index.html", home)

    # ---- section pages
    for n, (sid, fname, label, desc) in enumerate(PAGES):
        sub_header = (
            '<header id="top" class="sub"><div class="inner"><div class="eyebrow"><a href="./">%s</a> · %s</div>'
            "<h1>%s</h1><p>%s</p></div></header>"
        ) % (SITE, eyebrow.split(" · ")[0], label, html.escape(desc))
        prev_link = ('<a href="%s">← %s</a>' % (PAGES[n - 1][1], PAGES[n - 1][2])) if n else '<a href="./">← Start here</a>'
        next_link = ('<a href="%s">%s →</a>' % (PAGES[n + 1][1], PAGES[n + 1][2])) if n + 1 < len(PAGES) else '<a href="./">Back to the start →</a>'
        pager = '<div class="pager">%s<a href="./#sections">All sections</a>%s</div>' % (prev_link, next_link)
        body = relink(sections[sid], fname).replace("</section>", pager + "</section>")
        write(fname, page(fname, "%s – %s" % (label.replace("&", "and"), SITE), desc, sub_header, body))

    # ---- sitemap
    urls = [BASE] + [BASE + p[1] for p in PAGES]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join("  <url><loc>%s</loc></url>\n" % u for u in urls) + "</urlset>\n")
    print("built index.html and %d section pages" % len(PAGES))


if __name__ == "__main__":
    main()
