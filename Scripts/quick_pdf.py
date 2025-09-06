#!/usr/bin/env python3
"""
Quick PDF Converter - Single command solution
Just run: python quick_pdf.py
"""

def convert_to_pdf():
    """Simple one-liner PDF conversion"""
    
    # Try WeasyPrint first (most reliable)
    try:
        import weasyprint
        print("🔄 Converting with WeasyPrint...")
        
        html = weasyprint.HTML(filename="resume_clean.html")
        html.write_pdf("resume_clean.pdf")
        
        print("✅ SUCCESS! PDF created: resume_clean.pdf")
        print("📄 Margins and formatting preserved exactly")
        return True
        
    except ImportError:
        print("⚠️  WeasyPrint not available, trying Playwright...")
    except Exception as e:
        print(f"❌ WeasyPrint failed: {e}")
    
    # Try Playwright as backup
    try:
        from playwright.sync_api import sync_playwright
        import os
        
        print("🔄 Converting with Playwright...")
        
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Load the HTML file
            html_path = os.path.abspath("resume_clean.html")
            page.goto(f"file://{html_path}")
            
            # Generate PDF with no extra margins (CSS handles margins)
            page.pdf(
                path="resume_clean.pdf",
                format="A4",
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
                print_background=True,
                prefer_css_page_size=True
            )
            
            browser.close()
        
        print("✅ SUCCESS! PDF created: resume_clean.pdf")
        print("📄 Perfect web rendering with exact margins")
        return True
        
    except ImportError:
        print("⚠️  Playwright not available")
    except Exception as e:
        print(f"❌ Playwright failed: {e}")
    
    print("\n❌ PDF conversion failed!")
    print("\n🔧 To fix, install dependencies:")
    print("pip install weasyprint")
    print("or")
    print("pip install playwright && playwright install chromium")
    
    return False

if __name__ == "__main__":
    print("🎯 Quick Resume PDF Converter")
    print("=" * 30)
    
    import os
    if not os.path.exists("resume_clean.html"):
        print("❌ resume_clean.html not found!")
        input("Press Enter to exit...")
        exit(1)
    
    success = convert_to_pdf()
    
    if success:
        print("\n🎉 Done! Your PDF is ready for printing or sharing.")
    
    input("\nPress Enter to exit...")
