#!/usr/bin/env python3
"""
Resume HTML to PDF Converter
Converts resume_clean.html to PDF with exact margins preserved
"""

import os
from pathlib import Path

def convert_with_weasyprint():
    """Convert using WeasyPrint (best for CSS compatibility)"""
    try:
        import weasyprint
        
        html_file = "resume_clean.html"
        pdf_file = "resume_clean.pdf"
        
        # Convert HTML to PDF
        html_doc = weasyprint.HTML(filename=html_file)
        html_doc.write_pdf(pdf_file)
        
        print(f"✅ PDF created successfully: {pdf_file}")
        print("Margins and formatting preserved exactly as designed")
        
    except ImportError:
        print("❌ WeasyPrint not installed. Install with: pip install weasyprint")
    except Exception as e:
        print(f"❌ Error: {e}")

def convert_with_playwright():
    """Convert using Playwright (excellent for web-based rendering)"""
    try:
        from playwright.sync_api import sync_playwright
        
        html_file = Path("resume_clean.html").absolute()
        pdf_file = "resume_clean_playwright.pdf"
        
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Load the HTML file
            page.goto(f"file://{html_file}")
            
            # Generate PDF with exact A4 margins
            page.pdf(
                path=pdf_file,
                format="A4",
                margin={
                    "top": "0.5in",
                    "bottom": "0.5in", 
                    "left": "0.5in",
                    "right": "0.5in"
                },
                print_background=True,
                prefer_css_page_size=True
            )
            
            browser.close()
            
        print(f"✅ PDF created successfully: {pdf_file}")
        print("Perfect web rendering with exact margins")
        
    except ImportError:
        print("❌ Playwright not installed. Install with: pip install playwright")
        print("Then run: playwright install chromium")
    except Exception as e:
        print(f"❌ Error: {e}")

def convert_with_wkhtmltopdf():
    """Convert using wkhtmltopdf (lightweight option)"""
    try:
        import pdfkit
        
        html_file = "resume_clean.html"
        pdf_file = "resume_clean_wkhtml.pdf"
        
        # PDF options to preserve exact formatting
        options = {
            'page-size': 'A4',
            'margin-top': '0.5in',
            'margin-right': '0.5in',
            'margin-bottom': '0.5in',
            'margin-left': '0.5in',
            'encoding': "UTF-8",
            'no-outline': None,
            'enable-local-file-access': None,
            'print-media-type': None
        }
        
        pdfkit.from_file(html_file, pdf_file, options=options)
        
        print(f"✅ PDF created successfully: {pdf_file}")
        print("Lightweight conversion with preserved margins")
        
    except ImportError:
        print("❌ pdfkit not installed. Install with: pip install pdfkit")
        print("Also need wkhtmltopdf: https://wkhtmltopdf.org/downloads.html")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    print("🎯 Resume HTML to PDF Converter")
    print("=" * 40)
    
    # Check if HTML file exists
    if not os.path.exists("resume_clean.html"):
        print("❌ resume_clean.html not found in current directory")
        return
    
    print("Choose conversion method:")
    print("1. WeasyPrint (best CSS support)")
    print("2. Playwright (best rendering)")
    print("3. wkhtmltopdf (lightweight)")
    print("4. Try all methods")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        convert_with_weasyprint()
    elif choice == "2":
        convert_with_playwright()
    elif choice == "3":
        convert_with_wkhtmltopdf()
    elif choice == "4":
        print("\n🔄 Trying all methods...\n")
        convert_with_weasyprint()
        print()
        convert_with_playwright()
        print()
        convert_with_wkhtmltopdf()
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
