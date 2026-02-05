# 🎯 Job-Specific Resume Customization Guide

## Overview
This guide helps you create tailored resumes for specific job descriptions (JDs) by analyzing your base resume and customizing relevant sections to match job requirements.

## 📂 Project Structure
```
Resume Project/
├── README.md                  # This guide (project overview)
├── job_dashboard.html         # Analytics dashboard for applications
├── job_applications.csv       # Application tracking database
├── Master_Resume/             # Master template files
│   ├── resume_clean.html      # Master resume template
│   └── resume_clean.pdf       # Master resume PDF
├── Resume/                    # JD-specific resume management
│   ├── HTMLs/                 # JD-specific HTML files for editing
│   │   ├── resume_[JD-name].html
│   │   └── resume_[JD-name].html
│   ├── To_Apply/              # Generated PDFs ready for application
│   │   ├── resume_[JD-name].pdf
│   │   └── resume_[JD-name].pdf
│   └── Applied/               # Archive folder (manual organization)
└── Scripts/                   # Python automation scripts
    ├── create_jd_resume.py    # Create JD-specific HTML copies
    ├── convert_jd_pdf.py      # Convert HTML to PDF + log applications
    ├── update_dashboard.py    # Update dashboard with CSV data
    ├── serve_dashboard.py     # Local server for dashboard
    ├── view_applications.py   # CLI for application tracking
    └── quick_pdf.py           # Original PDF converter
```

## 🔍 Current Resume Analysis

### **Personal Information**
- **Name**: Naman Yeshwanth Kumar
- **Contact**: LinkedIn, GitHub, Email, Phone
- **Location**: Tempe, AZ (for education), Bengaluru, India (for previous work)

### **Education (3 entries)**
1. **Master of Science** - Computer Engineering (ASU, Expected May 2026)
   - GPA: 3.8/4.0
   - Courses: VLSI, Algorithms, Robotics, AI
2. **Nanodegree** - Self-Driving Car Engineer (Udacity, Feb 2023)
   - Focus: ML, Computer Vision, Path Planning
3. **Bachelor of Engineering** - Electrical & Electronics (BMS College, June 2022)

### **Technical Skills (4 categories)**
1. **HDLs/EDA**: SystemVerilog, Synopsys, Cadence tools
2. **Languages**: Python, C++, MATLAB, web technologies
3. **AI/Robotics**: ML, Computer Vision, ROS, Reinforcement Learning
4. **Tools/Hardware**: TensorFlow, PyTorch, Docker, Arduino, Raspberry Pi

### **Work Experience (2 positions)**
1. **Software Developer** - NCR GOLD (Oct 2022 - Apr 2024)
   - Django platform, Docker, AWS
2. **Research Intern** - Indian Institute of Science (Oct 2021 - Aug 2022)
   - Motor optimization, eVTOL research

### **Project Experience (3 projects)**
1. **Trezzit** - Full-stack expense app (Feb 2025 - Present)
2. **Intel Self-Checkout** - Open source contribution (Jan-Feb 2025)
3. **Raspberry Pi Self-Driving Car** - Autonomous vehicle (Feb-July 2022)

### **Awards & Honors (3 achievements)**
- DevHacks'25 Best AI Use Award
- Hack SoDA 2024 Second Place
- e-Yantra Top Ten Team

## 🎨 Customization Strategy

### **Level 1: Quick Wins (No content change)**
- Reorder sections by relevance
- Highlight relevant technical skills
- Emphasize matching projects/experience

### **Level 2: Content Optimization**
- Rewrite bullet points to match JD keywords
- Add/remove technical skills based on requirements
- Adjust project descriptions for relevance

### **Level 3: Structural Changes**
- Add relevant sections (e.g., Certifications, Publications)
- Remove less relevant sections
- Modify section titles (e.g., "Software Experience" vs "Work Experience")

## 📋 Step-by-Step Process

### **IMPORTANT: Collaborative Workflow**
This system uses a **human-in-the-loop** approach where the AI suggests changes and the user approves them before any edits are made.

### **Step 1: Analyze Job Description**
Identify key requirements:
- **Required Skills**: Programming languages, frameworks, tools
- **Preferred Experience**: Industry, project types, technologies
- **Education**: Degree requirements, relevant coursework
- **Keywords**: Buzzwords, industry terms, methodologies

### **Step 2: Create JD-Specific Copy**
```bash
powershell cmd 
cd "c:\Users\naman\Desktop\Resume Project\Scripts" ; python create_jd_resume.py "marvell-ai-platform-intern"

python create_jd_resume.py "company-role"
# Creates: resume_company-role.html (exact copy of master)
```

### **Step 3: AI Analysis & Suggestions**
The AI will analyze the JD and provide specific suggestions focused on:

**Primary Suggestions (High Impact):**
- **Section Reordering**: Most relevant sections first (Education → Skills → Experience → Projects)
- **Technical Skills Restructuring**: Reorder categories and prioritize JD-relevant skills
- **Keyword Integration**: Add missing JD keywords to existing skills/content
- **Category Reorganization**: Group related skills together for better relevance

**Secondary Suggestions (Content Enhancement):**
- **Bullet Point Keywords**: Add 1-2 relevant keywords to existing bullets
- **Minor Wording**: Small additions that don't change core content
- **Emphasis Shifts**: Highlight existing relevant experience

**🎨 Format Constraints (Critical):**
- **Line Length Balance**: Each skill category should fit ~1 line (avoid 2+ lines)
- **Visual Proportions**: Maintain balanced spacing across all categories
- **Smart Curation**: Remove less relevant skills when adding JD-specific ones
- **Addition/Removal Strategy**: Add JD keywords while removing non-essential items

**🛡️ Conservative Customization Rule (CRITICAL):**
- **Authenticity First**: Only use keywords and skills that genuinely exist in your background
- **Real Experience Only**: Don't add technologies you haven't actually used
- **JD Intersection**: Focus on the overlap between your real skills and JD requirements
- **Missing Keywords OK**: It's acceptable to miss some JD keywords if you don't have that experience
- **Genuine Representation**: Maintain honest representation of your capabilities

**⚠️ Focus**: Structural changes and keyword optimization rather than complete content rewrites

**⚠️ CRITICAL: No edits are made automatically. All suggestions require user approval.**

### **Step 4: User Review & Approval**
User reviews each suggestion and decides:
- ✅ **Accept**: "Yes, apply this change"
- ❌ **Reject**: "No, keep as is"
- 🔄 **Modify**: "Change it but differently"

### **Step 5: Apply Approved Changes**
Only after user confirmation, the AI applies the approved changes to the JD-specific HTML file.

### **Step 6: Review & Convert**
```bash
python convert_jd_pdf.py "company-role"
# Creates: resume_company-role.pdf
```

## 🔧 Customization Examples

### **Example 1: AI/ML Engineer Role**
**JD Keywords**: Machine Learning, TensorFlow, PyTorch, Computer Vision, Python

**Customizations:**
- **Skills Order**: AI/Robotics → Languages → Tools → HDLs
- **Highlighted Projects**: Trezzit (AI categorization), AdaptED AI
- **Experience Focus**: Research Intern (ML algorithms)
- **Added Keywords**: "deep learning", "neural networks", "model optimization"

### **Example 2: Full-Stack Developer Role**
**JD Keywords**: Django, React, JavaScript, Docker, AWS, Database

**Customizations:**
- **Skills Order**: Languages → Tools → AI/Robotics → HDLs
- **Highlighted Projects**: Trezzit (Django/React), NCR platform
- **Experience Focus**: Software Developer (Django, Docker, AWS)
- **Added Keywords**: "full-stack", "responsive design", "RESTful APIs"

### **Example 3: Hardware Engineer Role**
**JD Keywords**: VLSI, SystemVerilog, FPGA, Circuit Design, Embedded

**Customizations:**
- **Skills Order**: HDLs/EDA → Tools/Hardware → Languages → AI
- **Highlighted Education**: VLSI coursework, EEE degree
- **Experience Focus**: Research Intern (motor optimization, circuits)
- **Added Keywords**: "RTL design", "synthesis", "timing analysis"

## 🤖 Automation Features

### **Smart Keyword Matching**
- Analyzes JD for technical requirements
- Suggests skill prioritization
- Recommends content modifications

### **Content Suggestion Engine**
- Bullet point variations for different industries
- Action verb recommendations
- Quantification suggestions

### **Quality Checks**
- ATS optimization
- Keyword density analysis
- Length optimization (1-2 pages)

## 🎯 Best Practices

### **Content Guidelines**
1. **Quantify Everything**: Numbers, percentages, timelines
2. **Action Verbs**: Led, Developed, Optimized, Implemented
3. **Impact Focus**: Results, improvements, achievements
4. **Relevance First**: Most relevant experience prominently featured

### **ATS Optimization**
1. **Standard Fonts**: Times New Roman (already used)
2. **Clear Sections**: Consistent formatting maintained
3. **Keyword Rich**: Natural integration of JD terms
4. **Simple Layout**: Clean HTML structure preserved

### **Visual Consistency**
1. **Professional Format**: Maintained across all versions
2. **Print Ready**: Exact margins preserved
3. **Mobile Responsive**: Scalable design maintained

## 🎨 Smart Skills Curation Strategy

**Line Length Management:**
- **Target**: Each skill category fits in ~1 line for visual balance
- **Method**: Strategic addition/removal rather than just addition
- **Priority**: JD-relevant skills in, less relevant skills out

**Example Transformation:**
```
BEFORE: Languages: Python | C++ | MATLAB | Lua | PHP | JavaScript | HTML | CSS | SQL | Shell Script
AFTER:  Programming Languages: Python | C++ | MATLAB | JavaScript | SQL | Shell Script | Bash
```
**Changes**: Removed `Lua | PHP | HTML | CSS`, Added `Bash`, Changed category name

**Curation Rules:**
1. **Remove**: Skills not mentioned in JD and not core to your profile
2. **Add**: JD-specific keywords that you actually possess
3. **Reorder**: Most relevant skills first within each category
4. **Rename**: Categories to match JD terminology when appropriate

## 🔍 Quality Assurance

### **Pre-Application Checklist**
- [ ] All JD keywords naturally integrated
- [ ] Most relevant experience highlighted first
- [ ] Technical skills match job requirements
- [ ] Contact information updated
- [ ] PDF formatting verified
- [ ] File naming follows convention: `resume_[company-role].pdf`

### **Common Pitfalls to Avoid**
- ❌ Keyword stuffing without context
- ❌ Removing core competencies entirely
- ❌ Over-customization losing personal brand
- ❌ Forgetting to update contact information
- ❌ Inconsistent formatting between versions

## 📞 Usage Commands

```bash
# Create new JD-specific resume (outputs to Resume/To_Apply/)
python Scripts/create_jd_resume.py "google-swe"

# Convert to PDF and log application (outputs to To_Apply/)
python Scripts/convert_jd_pdf.py "google-swe"

# View application analytics dashboard
start job_dashboard.html
# OR serve locally: python Scripts/serve_dashboard.py

# Update dashboard with latest application data
python Scripts/update_dashboard.py

# View application tracking via CLI
python Scripts/view_applications.py

# Quick conversion of master resume
python Scripts/quick_pdf.py
```

## 🔄 Workflow Process

### **1. Create JD-Specific Resume**
```bash
python Scripts/create_jd_resume.py "tesla-optimus-simulation"
# Creates: Resume/HTMLs/resume_tesla-optimus-simulation.html
```

### **2. Customize & Convert**
- Edit the HTML file in `Resume/HTMLs/`
- Convert to PDF: `python Scripts/convert_jd_pdf.py "tesla-optimus-simulation"`
- PDF created in `Resume/To_Apply/` and application logged

### **3. Apply for Job**
- Use the PDF from `Resume/To_Apply/`
- Optionally organize files in `Resume/Applied/` after submission

### **4. Track Progress**
- View analytics: Open `job_dashboard.html`
- CLI tracking: `python Scripts/view_applications.py`

## 💡 Tips for Success

1. **Keep Master Updated**: Always update `resume_clean.html` with new experiences
2. **Version Control**: Track changes for different applications
3. **A/B Testing**: Try different customizations for similar roles
4. **Feedback Loop**: Update based on application results
5. **Regular Review**: Update base template quarterly

## ☁️ Cloud Automation (New!)
This project now supports **GitHub Actions** for fully automated PDF generation.

### **The Workflow**
1.  **Draft**: Use an AI agent (like GitHub Copilot) to create a resume.
    *   Command: `python Scripts/create_jd_resume.py "netflix-senior-swe"`
    *   This creates a file in `Resume/Drafts/`.
2.  **Push**: Commit and push your changes to GitHub.
3.  **Auto-Build**:
    *   GitHub Actions detects the new draft.
    *   It converts it to PDF automatically (using WeasyPrint).
    *   It moves the HTML to `Resume/HTMLs/` (archive).
    *   It commits the final PDF to `Resume/To_Apply/`.
4.  **Result**: Just `git pull` to get your fresh PDF!

## 💻 Local Automation
If you prefer running everything on your own machine:
1.  Create draft: `python Scripts/create_jd_resume.py "company-role"`
2.  Convert locally: `python Scripts/convert_jd_pdf.py "company-role"`
    *   *Requires `playwright` or `weasyprint` installed locally.*

---

**Last Updated**: September 2025  
**Author**: Resume Automation System  
**Version**: 1.0