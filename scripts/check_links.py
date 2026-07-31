#!/usr/bin/env python3
"""Validate internal links and fragments in the generated static site."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag == "a" and values.get("href"):
            self.links.append(values["href"] or "")


def resolve_target(
    site: Path, source: Path, link_path: str, base_path: str
) -> Path:
    if link_path.startswith("/"):
        normalized = link_path
        if base_path != "/" and (
            normalized == base_path.rstrip("/")
            or normalized.startswith(base_path)
        ):
            normalized = normalized[len(base_path.rstrip("/")) :]
        target = site / normalized.lstrip("/")
    else:
        target = source.parent / link_path
    if target.is_dir() or not target.suffix:
        target = target / "index.html"
    return target.resolve()


def main() -> None:
    if len(sys.argv) not in (2, 3):
        raise SystemExit("usage: check_links.py SITE_DIRECTORY [BASE_PATH]")
    site = Path(sys.argv[1]).resolve()
    base_path = sys.argv[2] if len(sys.argv) == 3 else "/"
    base_path = f"/{base_path.strip('/')}/" if base_path != "/" else "/"
    documents: dict[Path, DocumentParser] = {}
    errors: list[str] = []

    for html in site.rglob("*.html"):
        parser = DocumentParser()
        parser.feed(html.read_text(encoding="utf-8"))
        documents[html.resolve()] = parser

    for source, parser in documents.items():
        for raw_link in parser.links:
            parsed = urlsplit(raw_link)
            if parsed.scheme or parsed.netloc or raw_link.startswith(("mailto:", "tel:")):
                continue
            path = unquote(parsed.path)
            target = (
                source
                if not path
                else resolve_target(site, source, path, base_path)
            )
            if target not in documents:
                if target.exists() and not target.suffix == ".html":
                    continue
                errors.append(f"{source.relative_to(site)}: missing {raw_link}")
                continue
            if parsed.fragment and unquote(parsed.fragment) not in documents[target].ids:
                errors.append(
                    f"{source.relative_to(site)}: missing fragment {raw_link}"
                )

    if errors:
        print("\n".join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f"validated {len(documents)} HTML documents")


if __name__ == "__main__":
    main()
