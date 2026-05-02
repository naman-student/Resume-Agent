#!/usr/bin/env python3
"""
Convert tailored resume HTML files to PDFs for the current workflow.

Inputs live in Resume/Drafts/.
Outputs are written to Resume/To_Apply/.

This script intentionally does not update CSV files, move HTML files, or mutate
application status. Supabase/dashboard updates are handled separately.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DRAFTS_DIR = BASE_DIR / "Resume" / "Drafts"
TO_APPLY_DIR = BASE_DIR / "Resume" / "To_Apply"


def normalize_resume_name(name: str) -> str:
    cleaned = name.strip()
    if cleaned.endswith(".html"):
        cleaned = cleaned[:-5]
    if not cleaned.startswith("resume_"):
        cleaned = f"resume_{cleaned}"
    return cleaned


def find_input_html(name: str) -> Path:
    resume_name = normalize_resume_name(name)
    html_path = DRAFTS_DIR / f"{resume_name}.html"
    if not html_path.exists():
        raise FileNotFoundError(
            f"Could not find {html_path.relative_to(BASE_DIR)}. "
            "Create or copy the tailored HTML into Resume/Drafts first."
        )
    return html_path


def convert_with_weasyprint(html_path: Path, pdf_path: Path) -> None:
    import weasyprint

    html = weasyprint.HTML(filename=str(html_path))
    html.write_pdf(str(pdf_path))


def convert_with_playwright(html_path: Path, pdf_path: Path) -> None:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
        page.pdf(
            path=str(pdf_path),
            format="A4",
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            print_background=True,
            prefer_css_page_size=True,
        )
        browser.close()


def convert_resume(name: str) -> Path:
    html_path = find_input_html(name)
    TO_APPLY_DIR.mkdir(parents=True, exist_ok=True)
    pdf_path = TO_APPLY_DIR / f"{html_path.stem}.pdf"

    try:
        convert_with_weasyprint(html_path, pdf_path)
    except ImportError:
        convert_with_playwright(html_path, pdf_path)

    return pdf_path


def list_drafts() -> None:
    drafts = sorted(DRAFTS_DIR.glob("resume_*.html"))
    if not drafts:
        print("No draft HTML files found in Resume/Drafts.")
        return

    for draft in drafts:
        pdf_path = TO_APPLY_DIR / f"{draft.stem}.pdf"
        status = "pdf exists" if pdf_path.exists() else "no pdf"
        print(f"{draft.name}  [{status}]")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Convert Resume/Drafts HTML to Resume/To_Apply PDF.")
    parser.add_argument("name", nargs="?", help="Resume slug, filename, or resume_<slug>.html")
    parser.add_argument("--list", action="store_true", help="List available draft HTML files")
    args = parser.parse_args(argv)

    if args.list:
        list_drafts()
        return 0

    if not args.name:
        parser.error("name is required unless --list is used")

    try:
        pdf_path = convert_resume(args.name)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Created {pdf_path.relative_to(BASE_DIR)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
