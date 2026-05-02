#!/usr/bin/env python3
"""
resume_check.py — Resume feedback tool
Reads CI-generated PDFs from Resume/To_Apply/ (or any .pdf path you pass)
and reports: page count, section breakdown, bullet line estimates, word counts.

Usage:
    python Scripts/resume_check.py                        # all To_Apply/*.pdf
    python Scripts/resume_check.py Resume/To_Apply/foo.pdf
    python Scripts/resume_check.py Resume/To_Apply/a.pdf Resume/To_Apply/b.pdf
"""

import sys
import io
import re
from pathlib import Path

# Force UTF-8 on Windows console
if hasattr(sys.stdout, "buffer") and sys.stdout.encoding.lower() != "utf-8":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer, errors="replace")
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.buffer, errors="replace")

BASE_DIR = Path(__file__).parent.parent
TO_APPLY  = BASE_DIR / "Resume" / "To_Apply"

# ── PDF helpers ───────────────────────────────────────────────────────────────

def load_pdf(path: Path):
    from pypdf import PdfReader
    return PdfReader(str(path))


def page_count(reader) -> int:
    return len(reader.pages)


def extract_text_by_page(reader) -> list[str]:
    return [p.extract_text() or "" for p in reader.pages]


# ── Text analysis ─────────────────────────────────────────────────────────────

# Section headers as they appear in the PDF text
SECTION_HEADERS = [
    "SUMMARY", "SKILLS", "TECHNICAL SKILLS",
    "PROJECTS", "WORK EXPERIENCE", "EXPERIENCE",
    "EDUCATION", "AWARDS", "CERTIFICATIONS",
]

def split_into_sections(text: str) -> list[tuple[str, str]]:
    """Return [(section_name, section_body), ...] in order."""
    # Build a regex that matches any known header on its own line
    pattern = r"(?m)^(" + "|".join(re.escape(h) for h in SECTION_HEADERS) + r")\s*$"
    parts = re.split(pattern, text)
    # parts = [pre, header1, body1, header2, body2, ...]
    sections = []
    i = 1
    while i < len(parts) - 1:
        header = parts[i].strip()
        body   = parts[i + 1].strip()
        sections.append((header, body))
        i += 2
    return sections


def count_words(text: str) -> int:
    return len(text.split())


CHARS_PER_LINE = 105   # empirical for 9pt Times New Roman at ~6.8in text width

def line_estimate(text: str) -> float:
    """Rough printed-line count for a block of text."""
    return max(1.0, len(text) / CHARS_PER_LINE)


def split_bullets(body: str) -> list[str]:
    """
    Split section body into individual bullet strings.
    WeasyPrint PDF text has bullets as '●' or '•' or lines starting with them.
    Falls back to splitting on newlines.
    """
    # Try splitting on bullet characters
    raw = re.split(r"[●•◆▸\-]\s+", body)
    bullets = [b.strip().replace("\n", " ") for b in raw if b.strip()]
    if len(bullets) <= 1:
        # Fallback: non-empty lines
        bullets = [l.strip() for l in body.splitlines() if l.strip()]
    return bullets


# ── Formatting helpers ────────────────────────────────────────────────────────

W  = "⚠️ "
OK = "✅"
TI = "〰️ "
HR = "─" * 62


def page_flag(n: int) -> str:
    return OK if n == 1 else "❌"


def word_flag(n: int) -> str:
    if 1050 <= n <= 1400: return OK
    if n < 800 or n > 1600: return W
    return TI


def bullet_line_flag(lines: float) -> str:
    if lines <= 2.0: return OK
    if lines <= 2.8: return TI
    return W


# ── Main report ───────────────────────────────────────────────────────────────

def print_report(pdf_path: Path):
    print(f"\n{HR}")
    print(f"  {pdf_path.name}")
    print(HR)

    reader = load_pdf(pdf_path)
    pages  = page_count(reader)
    texts  = extract_text_by_page(reader)
    full   = "\n".join(texts)

    # ── Page count
    pf = page_flag(pages)
    print(f"\n  {pf} Pages          : {pages}")
    if pages > 1:
        print(f"       ❌ OVERFLOW — resume is {pages} pages. Trim content or tighten spacing.")

    # ── Word count
    total_words = count_words(full)
    wf = word_flag(total_words)
    print(f"  {wf} Total words     : {total_words}  (sweet spot 1050–1400)")

    # ── Sections
    sections = split_into_sections(full)

    if not sections:
        print("\n  ⚠️  Could not detect section headers in PDF text.")
        print("  Raw text preview:")
        print("  " + full[:400].replace("\n", "\n  "))
        print(f"\n{HR}\n")
        return

    print(f"\n  SECTIONS  ({len(sections)} found)")
    print(f"  {'─'*58}")

    total_bullets = 0

    for header, body in sections:

        if header in ("SUMMARY",):
            w = count_words(body)
            lines = line_estimate(body)
            wf2 = OK if 30 <= w <= 65 else W
            print(f"\n  {wf2} {header:<24} {w} words  (~{lines:.1f} lines)")

        elif header in ("SKILLS", "TECHNICAL SKILLS"):
            rows = [l.strip() for l in body.splitlines() if l.strip()]
            print(f"\n  📋 {header:<24} {len(rows)} rows")
            for row in rows:
                items = len(re.split(r"[|,]", row))
                lines = line_estimate(row)
                lf = OK if lines <= 1.4 else W
                label = row[:35] + ("…" if len(row) > 35 else "")
                print(f"       {lf} {label:<36} {items} items  (~{lines:.1f} lines)")

        elif header in ("EDUCATION", "AWARDS", "CERTIFICATIONS"):
            bullets = split_bullets(body)
            total_bullets += len(bullets)
            print(f"\n  🎓 {header:<24} {len(bullets)} items")
            for i, b in enumerate(bullets, 1):
                w = count_words(b)
                lines = line_estimate(b)
                lf = bullet_line_flag(lines)
                print(f"       {lf} item {i}: {w} words  (~{lines:.1f} lines)")

        else:  # PROJECTS, EXPERIENCE, WORK EXPERIENCE
            bullets = split_bullets(body)
            total_bullets += len(bullets)
            lines_total = sum(line_estimate(b) for b in bullets)
            print(f"\n  📁 {header:<24} {len(bullets)} bullets  ~{lines_total:.1f} total lines")

            # Try to group by entry (lines without bullet chars are usually titles)
            raw_lines = [l.strip() for l in body.splitlines() if l.strip()]
            current_entry = None
            entry_bullets: list[str] = []

            def flush_entry(title, blist):
                if not title and not blist:
                    return
                short = (title or "—")[:50] + ("…" if len(title or "") > 50 else "")
                nb = len(blist)
                el = sum(line_estimate(b) for b in blist)
                print(f"       📝 {short:<51} {nb}b  ~{el:.1f} lines")
                for j, b in enumerate(blist, 1):
                    w = count_words(b)
                    lines = line_estimate(b)
                    lf = bullet_line_flag(lines)
                    short_b = b[:70] + ("…" if len(b) > 70 else "")
                    print(f"            {lf} b{j}: {w}w  ~{lines:.1f}L  \"{short_b}\"")

            for line in raw_lines:
                is_bullet = bool(re.match(r"^[●•◆▸\-]", line))
                if is_bullet:
                    entry_bullets.append(re.sub(r"^[●•◆▸\-]\s*", "", line).strip())
                else:
                    # New entry title — flush previous
                    if current_entry is not None or entry_bullets:
                        flush_entry(current_entry or "", entry_bullets)
                    current_entry = line
                    entry_bullets = []
            flush_entry(current_entry or "", entry_bullets)

    print(f"\n  {'─'*58}")
    print(f"  📌 Total bullets (excl. skills/summary): {total_bullets}")

    # ── Final verdict
    print(f"\n  VERDICT")
    issues = []
    if pages > 1:
        issues.append(f"❌ {pages} pages — needs trimming")
    if total_words > 1400:
        issues.append(f"⚠️  Word count {total_words} is high")
    if total_words < 800:
        issues.append(f"⚠️  Word count {total_words} is low — resume may be sparse")

    if issues:
        for iss in issues:
            print(f"  {iss}")
    else:
        print(f"  ✅ Looks good — 1 page, word count in range")

    print(f"\n{HR}\n")


def main():
    targets: list[Path] = []

    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            p = Path(arg)
            if not p.is_absolute():
                p = BASE_DIR / p
            if p.exists():
                targets.append(p)
            else:
                print(f"Not found: {p}")
    else:
        targets = sorted(TO_APPLY.glob("*.pdf"))

    if not targets:
        print(f"No PDFs found in {TO_APPLY}")
        sys.exit(1)

    for t in targets:
        print_report(t)


if __name__ == "__main__":
    main()
