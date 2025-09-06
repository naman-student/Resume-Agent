#!/usr/bin/env python3
"""
Create Job-Specific Resume Copy
Creates a copy of resume_clean.html with JD-relevant naming for customization
"""

import os
import sys
import shutil
from datetime import datetime

def create_jd_resume(jd_name):
    """Create a JD-specific copy of the master resume"""
    
    # Validate input
    if not jd_name or not jd_name.strip():
        print("❌ Error: Please provide a JD name")
        print("Usage: python create_jd_resume.py 'company-role'")
        return False
    
    # Clean the JD name for filename
    jd_clean = jd_name.strip().lower().replace(' ', '-').replace('_', '-')
    jd_clean = ''.join(c for c in jd_clean if c.isalnum() or c in '-.')
    
    # Define file paths
    master_file = "../Master_Resume/resume_clean.html"
    output_dir = "../Resume/HTMLs"
    jd_file = os.path.join(output_dir, f"resume_{jd_clean}.html")
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Check if master file exists
    if not os.path.exists(master_file):
        print(f"❌ Error: Master resume file '{master_file}' not found!")
        print("Please ensure the file exists in Master_Resume/")
        return False
        print("Make sure you're in the correct directory with resume_clean.html")
        return False
    
    # Check if JD file already exists
    if os.path.exists(jd_file):
        response = input(f"⚠️  File '{jd_file}' already exists. Overwrite? (y/N): ")
        if response.lower() not in ['y', 'yes']:
            print("❌ Operation cancelled")
            return False
    
    try:
        # Read master file
        with open(master_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update title and add JD-specific comment
        updated_content = content.replace(
            '<title>Naman Yeshwanth Kumar - Resume</title>',
            f'<title>Naman Yeshwanth Kumar - Resume ({jd_name})</title>'
        )
        
        # Add JD-specific comment at the beginning
        jd_comment = f"""<!-- 
    JD-Specific Resume: {jd_name}
    Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    Base: resume_clean.html
    
    CUSTOMIZATION NOTES:
    - Update relevant sections based on job description
    - Prioritize matching technical skills
    - Highlight relevant projects and experience
    - Ensure ATS optimization with JD keywords
-->

"""
        
        # Insert comment after DOCTYPE
        updated_content = updated_content.replace(
            '<!DOCTYPE html>\\n',
            f'<!DOCTYPE html>\\n{jd_comment}'
        )
        
        # Write JD-specific file
        with open(jd_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✅ SUCCESS! Created JD-specific resume: Resume/HTMLs/{os.path.basename(jd_file)}")
        print(f"📄 Based on: Master_Resume/resume_clean.html")
        print(f"🎯 Job Description: {jd_name}")
        print()
        print("📋 NEXT STEPS:")
        print("1. Open the new HTML file in your editor")
        print("2. Analyze the job description requirements")
        print("3. Customize sections based on JD keywords:")
        print("   - Reorder Technical Skills by relevance")
        print("   - Highlight matching projects/experience")
        print("   - Update bullet points with JD keywords")
        print("   - Consider section reordering")
        print("4. Review and test the customized resume")
        print(f"5. Convert to PDF: python Scripts/convert_jd_pdf.py '{jd_clean}'")
        print(f"6. PDFs will be created in Resume/To_Apply/")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating JD resume: {e}")
        return False

def show_usage():
    """Show usage instructions and examples"""
    print("🎯 JD-Specific Resume Creator")
    print("=" * 40)
    print()
    print("USAGE:")
    print("  python create_jd_resume.py 'job-description-name'")
    print()
    print("EXAMPLES:")
    print("  python create_jd_resume.py 'google-swe'")
    print("  python create_jd_resume.py 'microsoft-ai-engineer'")
    print("  python create_jd_resume.py 'startup-fullstack'")
    print("  python create_jd_resume.py 'nvidia-hardware'")
    print()
    print("OUTPUT:")
    print("  Creates: resume_[cleaned-name].html")
    print("  Example: resume_google-swe.html")
    print()
    print("NAMING TIPS:")
    print("  - Use company-role format")
    print("  - Keep it short and descriptive")
    print("  - Avoid special characters")
    print("  - Use hyphens instead of spaces")

def analyze_current_resumes():
    """Show existing resume files"""
    html_files = [f for f in os.listdir('.') if f.startswith('resume_') and f.endswith('.html')]
    pdf_files = [f for f in os.listdir('.') if f.startswith('resume_') and f.endswith('.pdf')]
    
    if html_files or pdf_files:
        print("📁 EXISTING JD-SPECIFIC RESUMES:")
        print("-" * 35)
        
        # Group by base name
        base_names = set()
        for f in html_files + pdf_files:
            base_name = f.replace('resume_', '').rsplit('.', 1)[0]
            base_names.add(base_name)
        
        for base_name in sorted(base_names):
            html_exists = f"resume_{base_name}.html" in html_files
            pdf_exists = f"resume_{base_name}.pdf" in pdf_files
            
            status = []
            if html_exists:
                status.append("HTML ✅")
            if pdf_exists:
                status.append("PDF ✅")
            
            print(f"  {base_name}: {' | '.join(status)}")
        
        print()

def main():
    """Main function"""
    print("🎯 JD-Specific Resume Creator")
    print("=" * 40)
    
    # Show existing resumes
    analyze_current_resumes()
    
    # Check command line arguments
    if len(sys.argv) != 2:
        show_usage()
        return
    
    jd_name = sys.argv[1]
    
    # Create JD-specific resume
    success = create_jd_resume(jd_name)
    
    if success:
        print()
        print("🎉 Ready to customize your resume for this specific job!")
        print("📖 See README.md for detailed customization guide")

if __name__ == "__main__":
    main()