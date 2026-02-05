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

# Import WeasyPrint (must be installed in CI)
import csv

def update_dashboard_data():
    """Update the dashboard HTML with fresh CSV data"""
    csv_file = os.path.join(BASE_DIR, "job_applications.csv")
    dashboard_file = os.path.join(BASE_DIR, "job_dashboard.html")
    
    if not os.path.exists(csv_file) or not os.path.exists(dashboard_file):
        return False
    
    try:
        # Read CSV data
        with open(csv_file, 'r', encoding='utf-8') as f:
            csv_content = f.read().strip()
        
        # Read dashboard HTML
        with open(dashboard_file, 'r', encoding='utf-8') as f:
            dashboard_content = f.read()
        
        # Find and replace the CSV data section
        start_marker = "const csvText = `"
        end_marker = "`;"
        
        start_idx = dashboard_content.find(start_marker)
        if start_idx == -1:
            return False
        
        start_idx += len(start_marker)
        end_idx = dashboard_content.find(end_marker, start_idx)
        if end_idx == -1:
            return False
        
        # Replace the CSV data
        new_dashboard = (
            dashboard_content[:start_idx] + 
            csv_content + 
            dashboard_content[end_idx:]
        )
        
        # Write updated dashboard
        with open(dashboard_file, 'w', encoding='utf-8') as f:
            f.write(new_dashboard)
        print("🎯 Dashboard updated with fresh data!")
        return True
    except Exception as e:
        print(f"⚠️  Warning: Could not update dashboard: {e}")
        return False

def log_application(jd_name, html_file, pdf_file):
    """Log application details to CSV tracking file"""
    try:
        csv_file = os.path.join(BASE_DIR, "job_applications.csv")
        
        # Parse company and position from jd_name
        # clean up jd_name which might be file basename
        clean_name = jd_name.replace("resume_", "").replace(".html", "")
        parts = clean_name.replace('-', ' ').title().split()
        if len(parts) >= 2:
            company = parts[0]
            position = ' '.join(parts[1:])
        else:
            company = clean_name.title()
            position = "Unknown Position"
        
        # Get current timestamp
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        
        # Prepare row data - using ../Resume/ format to match existing CSV
        html_rel = f"../Resume/HTMLs/{os.path.basename(html_file)}"
        pdf_rel = f"../Resume/To_Apply/{os.path.basename(pdf_file)}"
        
        row_data = [
            date_str,
            time_str,
            company,
            position,
            html_rel,
            pdf_rel,
            "PDF Created",
            f"Auto-generated from {clean_name}"
        ]
        
        # Check if CSV exists, create with headers if not
        file_exists = os.path.exists(csv_file)
        
        with open(csv_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Add headers if file is new
            if not file_exists:
                headers = ["Date", "Time", "Company", "Position", "Resume_File", "PDF_File", "Status", "Notes"]
                writer.writerow(headers)
            
            writer.writerow(row_data)
        
        print(f"📊 Application logged to {csv_file}")
        
        # Update dashboard with fresh data
        update_dashboard_data()
        
        return True
        
    except Exception as e:
        print(f"⚠️  Warning: Could not log to CSV: {e}")

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

            # 3. Log to CSV
            print(f"  - Logging to CSV...")
            log_application(base_name, final_html_path, pdf_path)

        except Exception as e:
            print(f"  ❌ Failed to process {draft}: {e}")
            # We do NOT exit, we try the next one

if __name__ == "__main__":
    ensure_dirs()
    process_resumes()
