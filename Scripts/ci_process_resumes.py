#!/usr/bin/env python3
"""
CI Process Resumes
Run by GitHub Actions to process drafts:
1. Convert Drafts/*.html -> To_Apply/*.pdf
2. Move Drafts/*.html -> HTMLs/*.html
"""

import os
import shutil
import sys
from datetime import datetime

# Define paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRAFTS_DIR = os.path.join(BASE_DIR, "Resume", "Drafts")
HTMLS_DIR = os.path.join(BASE_DIR, "Resume", "HTMLs")
PDF_DIR = os.path.join(BASE_DIR, "Resume", "To_Apply")

def ensure_dirs():
    for d in [DRAFTS_DIR, HTMLS_DIR, PDF_DIR]:
        os.makedirs(d, exist_ok=True)

def process_resumes():
    # Check for drafts
    if not os.path.exists(DRAFTS_DIR):
        print("No Drafts directory found.")
        return

    drafts = [f for f in os.listdir(DRAFTS_DIR) if f.endswith('.html')]
    
    if not drafts:
        print("No drafts to process.")
        return

    print(f"found {len(drafts)} drafts to process...")
    
    # Import WeasyPrint (must be installed in CI)
    try:
        import weasyprint
    except ImportError:
        print("Error: WeasyPrint not installed. This script is intended for CI environment.")
        sys.exit(1)

    for draft in drafts:
        draft_path = os.path.join(DRAFTS_DIR, draft)
        base_name = os.path.splitext(draft)[0]
        pdf_name = f"{base_name}.pdf"
        pdf_path = os.path.join(PDF_DIR, pdf_name)
        final_html_path = os.path.join(HTMLS_DIR, draft)

        print(f"Processing: {draft}")
        
        try:
            # 1. Convert to PDF
            print(f"  - Converting to PDF...")
            html = weasyprint.HTML(filename=draft_path)
            html.write_pdf(pdf_path)
            print(f"    Success: {pdf_name}")

            # 2. Move HTML to Archive
            print(f"  - Archiving HTML...")
            shutil.move(draft_path, final_html_path)
            print(f"    Moved to HTMLs/")

        except Exception as e:
            print(f"  ❌ Failed to process {draft}: {e}")
            # We do NOT exit, we try the next one

if __name__ == "__main__":
    ensure_dirs()
    process_resumes()
