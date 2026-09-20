# AI Resume Screening & Job Match System

## Project Overview

A local Streamlit dashboard that compares a PDF resume with a job description. It extracts resume text, preprocesses it, calculates a genuine TF-IDF/cosine-similarity match score, identifies technical skill gaps, recommends roles transparently, and presents the results with Plotly charts. It uses no paid service, API key, or neural network.

## Problem Statement
Recruiters and students need a quick, explainable way to compare resume content with job requirements. Manual comparison is time-consuming, while opaque scores are difficult to defend in a viva.

## Objectives
- Extract and clean resume text from PDFs.
- Calculate an actual resume–job similarity percentage.
- Identify candidate, matching, and missing skills.
- Provide evidence-based rule-based role recommendations.
- Offer actionable, honest improvement suggestions through a professional dashboard.

## Key Features
- PDF upload with friendly invalid/empty/scanned-PDF handling.
- Demo Mode labelled “Demo Candidate — For Demonstration Purposes Only”.
- Three editable sample job descriptions and custom JD support.
- TF-IDF vectorization and cosine similarity.
- Case-insensitive predefined technical skill extraction.
- Matching/missing skills, role coverage table, and Plotly visualizations.
- Modular backend in `utils/` and no external API dependency.

## Technology Stack
Python, Streamlit, scikit-learn, PyMuPDF, pandas, NumPy, and Plotly.

## System Architecture
```text
PDF resume → PyMuPDF text extraction → preprocessing → TF-IDF vectors
          → cosine similarity → percentage/category
          → skill extraction → matching/missing skills
          → role coverage → suggestions → Streamlit dashboard
```

## Methodology
### TF-IDF
Term Frequency–Inverse Document Frequency gives higher weight to words that are important in the document but less common across the resume and job description pair. `TfidfVectorizer` performs this conversion.

### Cosine Similarity
Cosine similarity compares the angle between the two TF-IDF vectors. A value near 1 means the documents use similar terms. The application displays `similarity × 100` as the match score; it is never hardcoded. Categories are Excellent (80–100), Good (60–79), Moderate (40–59), and Low (below 40).

### Skill Extraction
A readable dictionary of canonical skills and aliases is searched case-insensitively in the resume and JD. This is rule-based extraction, not a claim that a skill is present unless its text is found.

### Skill-Based Role Recommendation
The five role mappings in `utils/role_recommender.py` calculate `detected required skills / all required skills × 100`. This is a transparent rule-based recommendation system, not a trained AI model.

## Project Structure
```text
AI_Resume_Screening_Job_Match/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── sample_resume.txt
└── utils/
    ├── __init__.py
    ├── pdf_extractor.py
    ├── text_processing.py
    ├── skill_extractor.py
    ├── matcher.py
    └── role_recommender.py
```

## Installation
From this folder:
```bash
python -m venv .venv
```
Windows:
```bat
.venv\Scripts\activate
```
Then:
```bash
pip install -r requirements.txt
```

## VS Code Setup
1. Open the repository in VS Code.
2. Open `AI_Resume_Screening_Job_Match` as the working folder.
3. Select the `.venv` Python interpreter (`Ctrl+Shift+P` → Python: Select Interpreter).
4. Open a new terminal and install the requirements.

## How to Run
```bash
cd AI_Resume_Screening_Job_Match
streamlit run app.py
```
The browser normally opens at `http://localhost:8501`.

## Demo Instructions
1. Start with Demo Mode enabled.
2. Select Data Scientist, Data Analyst, or Machine Learning Engineer.
3. Edit the job description if desired.
4. Click **Analyze Resume** and inspect the score, charts, skills, recommendations, and suggestions.
5. Disable Demo Mode and upload a text-based PDF to test a real resume.
6. Use `sample_resume.txt` as content for creating a local demonstration PDF if needed.

## Expected Output
The dashboard shows an actual percentage and category, a match/gap chart, skill lists, a role coverage table, and suggestions based on skills missing from the selected JD.

## Screenshots
_Add screenshots of the running dashboard here for the internship report._

## Limitations
- Keyword skill extraction can miss synonyms and does not understand context or proficiency.
- Text-based PDFs work best; scanned image PDFs require OCR.
- TF-IDF measures textual overlap rather than true semantic understanding.
- Recommendations are transparent heuristics and should support—not replace—human review.

## Future Scope
OCR support, synonym/ontology matching, multilingual preprocessing, richer experience extraction, recruiter export reports, and evaluation on a labelled resume–JD dataset.

## Conclusion
This project demonstrates an understandable end-to-end NLP pipeline using reproducible local tools. Its calculated score and explainable skill rules make it appropriate for a university internship demonstration and viva.
