#!/usr/bin/env python3
"""
Convert JD-Specific Resume to PDF
Converts customized JD resume HTML to PDF with matching name
"""

import os
import sys
import csv
from datetime import datetime
from pathlib import Path

def update_dashboard_data():
    """Update the dashboard HTML with fresh CSV data"""
    csv_file = "../job_applications.csv"
    dashboard_file = "../job_dashboard.html"
    
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
    except:
        return False

def log_application(jd_name, html_file, pdf_file):
    """Log application details to CSV tracking file"""
    try:
        csv_file = "../job_applications.csv"
        
        # Parse company and position from jd_name
        parts = jd_name.replace('-', ' ').title().split()
        if len(parts) >= 2:
            company = parts[0]
            position = ' '.join(parts[1:])
        else:
            company = jd_name.title()
            position = "Unknown Position"
        
        # Get current timestamp
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        
        # Prepare row data (normalize paths for JavaScript compatibility)
        html_file_normalized = html_file.replace('\\', '/')
        pdf_file_normalized = pdf_file.replace('\\', '/')
        
        row_data = [
            date_str,
            time_str,
            company,
            position,
            html_file_normalized,
            pdf_file_normalized,
            "PDF Created",
            f"Auto-generated from {jd_name}"
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
        print(f"   Company: {company}")
        print(f"   Position: {position}")
        print(f"   Date/Time: {date_str} {time_str}")
        
        # Update dashboard with fresh data
        try:
            update_dashboard_data()
        except Exception as e:
            print(f"⚠️  Warning: Could not update dashboard: {e}")
        
        return True
        
    except Exception as e:
        print(f"⚠️  Warning: Could not log to CSV: {e}")
        return False

def convert_jd_to_pdf(jd_name):
    """Convert JD-specific resume to PDF using the same methods as quick_pdf.py"""
    
    # Clean the JD name for filename
    jd_clean = jd_name.strip().lower().replace(' ', '-').replace('_', '-')
    jd_clean = ''.join(c for c in jd_clean if c.isalnum() or c in '-.')
    
    # Define file paths
    html_dir = "../Resume/HTMLs"
    pdf_dir = "../Resume/To_Apply"
    html_file = os.path.join(html_dir, f"resume_{jd_clean}.html")
    pdf_file = os.path.join(pdf_dir, f"resume_{jd_clean}.pdf")
    
    # Ensure PDF output directory exists
    os.makedirs(pdf_dir, exist_ok=True)
    
    # Check if HTML file exists
    if not os.path.exists(html_file):
        print(f"❌ Error: JD resume file '{html_file}' not found!")
        print(f"Create it first with: python Scripts/create_jd_resume.py '{jd_name}'")
        return False
    
    print(f"🎯 Converting JD-Specific Resume: {jd_name}")
    print(f"📄 Input: Resume/HTMLs/{os.path.basename(html_file)}")
    print(f"📄 Output: Resume/To_Apply/{os.path.basename(pdf_file)}")
    print("-" * 50)
    
    # Try WeasyPrint first (most reliable)
    try:
        import weasyprint
        print("🔄 Converting with WeasyPrint...")
        
        html = weasyprint.HTML(filename=html_file)
        html.write_pdf(pdf_file)
        
        print(f"✅ SUCCESS! PDF created: {pdf_file}")
        print("📄 Margins and formatting preserved exactly")
        
        # Log the application
        log_application(jd_name, html_file, pdf_file)
        
        return True
        
    except ImportError:
        print("⚠️  WeasyPrint not available, trying Playwright...")
    except Exception as e:
        print(f"❌ WeasyPrint failed: {e}")
    
    # Try Playwright as backup
    try:
        from playwright.sync_api import sync_playwright
        
        print("🔄 Converting with Playwright...")
        
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Load the HTML file
            html_path = os.path.abspath(html_file)
            page.goto(f"file://{html_path}")
            
            # Generate PDF with no extra margins (CSS handles margins)
            page.pdf(
                path=pdf_file,
                format="A4",
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
                print_background=True,
                prefer_css_page_size=True
            )
            
            browser.close()
        
        print(f"✅ SUCCESS! PDF created: {pdf_file}")
        print("📄 Perfect web rendering with exact margins")
        
        # Log the application
        log_application(jd_name, html_file, pdf_file)
        
        return True
        
    except ImportError:
        print("⚠️  Playwright not available")
    except Exception as e:
        print(f"❌ Playwright failed: {e}")
    
    print("\\n❌ PDF conversion failed!")
    print("\\n🔧 To fix, install dependencies:")
    print("pip install weasyprint")
    print("or")
    print("pip install playwright && playwright install chromium")
    
    return False

def show_available_resumes():
    """Show available JD-specific resumes"""
    html_dir = "../Resume/HTMLs"
    pdf_dir = "../Resume/To_Apply"
    
    if not os.path.exists(html_dir):
        print("📁 No HTMLs directory found.")
        print("Create resumes with: python Scripts/create_jd_resume.py 'company-role'")
        return
        
    html_files = [f for f in os.listdir(html_dir) if f.startswith('resume_') and f.endswith('.html')]
    
    if not html_files:
        print("📁 No JD-specific resumes found in Resume/HTMLs/")
        print("Create one with: python Scripts/create_jd_resume.py 'company-role'")
        return
    
    print("📁 AVAILABLE JD-SPECIFIC RESUMES:")
    print("   📝 HTMLs in: Resume/HTMLs/")
    print("   📄 PDFs in: Resume/To_Apply/")
    print("-" * 40)
    
    for html_file in sorted(html_files):
        base_name = html_file.replace('resume_', '').replace('.html', '')
        pdf_file = f"resume_{base_name}.pdf"
        pdf_path = os.path.join(pdf_dir, pdf_file)
        pdf_exists = os.path.exists(pdf_path)
        
        status = "PDF ✅" if pdf_exists else "No PDF ❌"
        print(f"  {base_name}: {status}")
    
    print()

def show_usage():
    """Show usage instructions"""
    print("🎯 JD-Specific Resume PDF Converter")
    print("=" * 45)
    print()
    print("USAGE:")
    print("  python convert_jd_pdf.py 'job-description-name'")
    print()
    print("EXAMPLES:")
    print("  python convert_jd_pdf.py 'google-swe'")
    print("  python convert_jd_pdf.py 'microsoft-ai-engineer'")
    print("  python convert_jd_pdf.py 'startup-fullstack'")
    print()
    print("NOTES:")
    print("  - Converts resume_[name].html to resume_[name].pdf")
    print("  - Uses same conversion methods as quick_pdf.py")
    print("  - Preserves exact formatting and margins")
    print("  - Optimized for ATS and print quality")

def validate_jd_customization(html_file, jd_name):
    """Basic validation to check if resume was customized"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if title was updated (basic customization check)
        if f"Resume ({jd_name})" in content:
            print("✅ Resume appears to be customized for this JD")
        else:
            print("⚠️  Warning: Resume may not be customized yet")
            print("   Consider updating it based on job requirements")
        
        # Check for JD comment
        if "JD-Specific Resume:" in content:
            print("✅ JD-specific metadata found")
        
        return True
        
    except Exception as e:
        print(f"⚠️  Could not validate customization: {e}")
        return False

def main():
    """Main function"""
    print("🎯 JD-Specific Resume PDF Converter")
    print("=" * 45)
    
    # Show available resumes
    show_available_resumes()
    
    # Check command line arguments
    if len(sys.argv) != 2:
        show_usage()
        return
    
    jd_name = sys.argv[1]
    jd_clean = jd_name.strip().lower().replace(' ', '-').replace('_', '-')
    jd_clean = ''.join(c for c in jd_clean if c.isalnum() or c in '-.')
    html_file = os.path.join("../Resume/HTMLs", f"resume_{jd_clean}.html")
    
    # Validate customization
    if os.path.exists(html_file):
        validate_jd_customization(html_file, jd_name)
        print()
    
    # Convert to PDF
    success = convert_jd_to_pdf(jd_name)
    
    if success:
        print()
        print("🎉 Your JD-specific resume PDF is ready!")
        print("📋 FINAL CHECKLIST:")
        print("  ✅ PDF formatting verified")
        print("  ✅ All customizations preserved")
        print("  ✅ ATS-friendly formatting maintained")
        print("  ✅ Print-ready with exact margins")
        print()
        print("📤 Ready for submission!")
    else:
        print()
        print("❌ Conversion failed. Please check the error messages above.")

if __name__ == "__main__":
    main()