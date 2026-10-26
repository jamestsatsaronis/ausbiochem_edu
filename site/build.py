#!/usr/bin/env python3
"""Build the GitHub Pages copy of the ASBMB Education Feature archive.

The article pages (education-feature-*.html) and the page templates are made
for the ASBMB website. They set <base href="https://www.asbmb.org.au/">, so
their relative links and image paths resolve against that site. This script
copies them into a static site that works anywhere, keeping the ASBMB layout:

- the home page is the website's Australian Biochemist Education Feature page
  (templates/asbmb-education-feature-page.html) with the article list from
  website/education-page-article-links.html added after its Contributing
  section;
- the <base> element is removed, so each article's images/ folder loads from
  beside its page;
- links to other pages of the ASBMB website are made absolute, so the menu
  still goes to www.asbmb.org.au;
- the menu's Australian Biochemist Education Feature link, and each article's
  "< Back to Education" link, go to the home page.

Usage:
    python3 site/build.py              # writes to _site/
    python3 site/build.py --out DIR
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ASBMB = "https://www.asbmb.org.au/"

BASE = re.compile(r'\s*<base href="https://www\.asbmb\.org\.au/"\s*/?>')
LINK = re.compile(r'(<a\b[^>]*?\bhref=")([^"]*)(")')
ISSUE_DIR = re.compile(r"^vol-\d+-no-\d+-[a-z]+$")
HOME_PAGE = "australian-biochemist-education-feature"
# Each article ends with this link; here it returns to the article list on the home page.
BACK_LINK = re.compile(r'(<a href=")education("[^>]*>&lt; Back to Education</a>)')
# The article list goes after the Contributing section of the home page.
INSERT_AFTER = "on how to contribute.</span></div></div><div><br></div></div>"


def localise(html, pages):
    """Rewrite an ASBMB website page so that it works away from www.asbmb.org.au.

    pages maps ASBMB page names to addresses on this site, relative to the
    page; links to any other ASBMB page go to www.asbmb.org.au.
    """
    html, found = BASE.subn("", html, count=1)
    if not found:
        raise ValueError("page has no ASBMB <base> element")

    def fix(m):
        url = m.group(2)
        if re.match(r"(?:[a-z]+:|#|//)", url) or url.startswith("images/"):
            return m.group(0)
        url = pages.get(url, ASBMB + url)
        return m.group(1) + url + m.group(3)

    return LINK.sub(fix, html)


def find_articles():
    """Return {page name: article folder} for every article page in the archive."""
    articles = {}
    for year in sorted(p for p in REPO.iterdir() if re.fullmatch(r"\d{4}", p.name)):
        for issue in sorted(p for p in year.iterdir() if ISSUE_DIR.match(p.name)):
            for folder in sorted(p for p in issue.iterdir() if p.is_dir()):
                page = folder / f"education-feature-{folder.name}.html"
                if page.exists():
                    articles[page.stem] = folder
    return articles


def build(out):
    articles = find_articles()

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    for name, folder in articles.items():
        rel = folder.relative_to(REPO)
        dest = out / rel
        dest.mkdir(parents=True)
        home = "../" * len(rel.parts) + "index.html"
        html = (folder / f"{name}.html").read_text(encoding="utf-8")
        html, found = BACK_LINK.subn(rf"\g<1>{HOME_PAGE}\g<2>", html)
        if found != 1:
            raise ValueError(f"{name}: expected one link back to Education, found {found}")
        page = localise(html, {HOME_PAGE: home})
        (dest / f"{name}.html").write_text(page, encoding="utf-8")
        if (folder / "images").is_dir():
            shutil.copytree(folder / "images", dest / "images")

    links = (REPO / "website" / "education-page-article-links.html").read_text(encoding="utf-8")
    links = re.sub(r"<!--.*?-->\s*", "", links, flags=re.S).strip()
    missing = set(re.findall(r'href="(education-feature-[^"]+)"', links)) - set(articles)
    if missing:
        raise ValueError(f"article list links to pages that are not in the archive: {sorted(missing)}")

    template = (REPO / "templates" / "asbmb-education-feature-page.html").read_text(encoding="utf-8")
    if template.count(INSERT_AFTER) != 1:
        raise ValueError("cannot find where to add the article list in the Education Feature page template")
    page = template.replace(INSERT_AFTER, INSERT_AFTER + links)
    pages = {name: f"{folder.relative_to(REPO).as_posix()}/{name}.html" for name, folder in articles.items()}
    pages[HOME_PAGE] = "index.html"
    (out / "index.html").write_text(localise(page, pages), encoding="utf-8")

    print(f"Built the Education Feature page and {len(articles)} article pages to {out}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--out", type=Path, default=REPO / "_site", help="output folder (default: _site)")
    args = parser.parse_args()
    build(args.out.resolve())


if __name__ == "__main__":
    sys.exit(main())
