# GitHub Copilot Repository Instructions

This repository contains a **Career Resume Automation System**.
When helping the user, ALWAYS follow these rules:

## 🚀 Workflow Rules (CRITICAL)
1.  **NEVER try to generate PDFs directly.**
    *   The environment usually lacks `weasyprint` or `playwright`.
    *   Instead, focus on creating the **HTML draft**.
2.  **Creation Process:**
    *   Run `python Scripts/create_jd_resume.py "company-role"` to start.
    *   This creates a file in `Resume/Drafts/`.
3.  **Editing Process:**
    *   Edit the HTML file in `Resume/Drafts/`.
    *   Tailor the content to the Job Description (JD).
    *   **Do not** move the file yourself.
4.  **Finalization:**
    *   Once the HTML is ready, tell the user to **PUSH** to GitHub.
    *   The GitHub Action (`generate_pdfs.yml`) will handle the PDF conversion.

## 🛠️ Style Guide
- **HTML/CSS:** Use the existing structure in `Master_Resume/resume_clean.html`.
- **Formatting:** Maintain the exact CSS classes (`section`, `header`, `bullet-point`) to ensure the PDF looks correct.
- **Tone:** Professional, quantifiable results, action verbs.
