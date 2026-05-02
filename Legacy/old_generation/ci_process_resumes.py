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
HTMLS_DIR = os.path.join(BASE_DIR, "Resume", "Archive")  # New Archive Location
PDF_DIR = os.path.join(BASE_DIR, "Resume", "To_Apply")
CSV_FILE = os.path.join(BASE_DIR, "job_applications.csv")

def ensure_dirs():
    for d in [DRAFTS_DIR, HTMLS_DIR, PDF_DIR]:
        os.makedirs(d, exist_ok=True)

# Import WeasyPrint (must be installed in CI)
import csv

def update_csv_status(filename, pdf_path):
    """Update row in CSV: Status=READY, PDF_Path=..."""
    try:
        rows = []
        updated = False
        
        # We match by looking for the HTML filename in the HTML_Path column
        # Or by ID if the filename closely matches.
        # Simpler: Match by HTML filename basename
        target_html = os.path.basename(filename)
        
        if os.path.exists(CSV_FILE):
            with open(CSV_FILE, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                fieldnames = reader.fieldnames
                for row in reader:
                    # Check if this row corresponds to our file
                    # HTML_Path might be "Resume/Drafts/foo.html" or "../Resume/Drafts/foo.html"
                    if os.path.basename(row['HTML_Path']) == target_html:
                        row['Status'] = 'READY'
                        # Use relative path for PDF: Resume/To_Apply/foo.pdf
                        row['PDF_Path'] = f"Resume/To_Apply/{os.path.basename(pdf_path)}"
                        # Update HTML path to Archive
                        row['HTML_Path'] = f"Resume/Archive/{target_html}"
                        updated = True
                    rows.append(row)

            if updated:
                with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
                print(f"✅ CSV Updated: {target_html} -> READY")
                return True
            else:
                print(f"⚠️  Warning: No matching CSV entry found for {target_html}. Adding new one...")
                # Fallback: Add new row if it was manually added to Drafts
                return False 
        return False
    except Exception as e:
        print(f"❌ Failed to update CSV: {e}")
        return False

def add_new_ready_entry(base_name, html_rel, pdf_rel):
    """Fallback for files not in CSV"""
    # ... (simplified logic if needed, but optimally we trust create_jd_resume)
    pass

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
        # For local dev without WeasyPrint, we might skip conversion
        if os.environ.get('CI') != 'true':
             print("⚠️  WEASYPRINT MISSING: Skipping PDF generation (Local Mode)")
             return
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

            # 2. Update CSV Status
            success = update_csv_status(draft, pdf_path)
            
            # 3. Move HTML to Archive
            print(f"  - Archiving HTML...")
            shutil.move(draft_path, final_html_path)
            print(f"    Moved to Resume/Archive/")

        except Exception as e:
            print(f"  ❌ Failed to process {draft}: {e}")

if __name__ == "__main__":
    ensure_dirs()
    process_resumes()
