# AI Resume Screening & Job Match System

An AI-powered Resume Screening and Job Matching web application built using Python, Streamlit, Natural Language Processing (NLP), and Machine Learning techniques.

The system analyzes a candidate's PDF resume against a selected or custom job description and provides a transparent resume-to-job match score, skill analysis, missing skills, and skill-based role recommendations.

## 🚀 Live Demo

**Live Application:**  
https://anushka13102003-2023-27-ai-resume-screening-job-matchapp-a1xzq.streamlit.app

The application allows users to upload a PDF resume and interactively analyze it against different job descriptions.

---

## 📌 Project Overview

Recruiters often need to screen a large number of resumes for a particular job role. Manually comparing resumes with job descriptions can be time-consuming and inconsistent.

This project provides an automated resume screening system that uses NLP-based text similarity and skill extraction to compare a candidate's resume with a job description.

### Main Workflow

PDF Resume  
↓  
Text Extraction  
↓  
Text Preprocessing  
↓  
TF-IDF Vectorization  
↓  
Cosine Similarity  
↓  
Resume–Job Match Score  
↓  
Skill Extraction  
↓  
Matching & Missing Skills  
↓  
Skill-Based Role Recommendation  
↓  
Resume Insights & Suggestions

---

## 🎯 Objectives

- Automatically extract text from PDF resumes.
- Compare resumes with job descriptions.
- Calculate a transparent resume-to-job similarity score.
- Identify candidate skills.
- Identify matching skills.
- Identify missing or required skills.
- Recommend suitable job roles based on detected skills.
- Provide visual analysis of the matching and missing skills.
- Provide actionable resume improvement suggestions.
- Build an interactive and easy-to-use web interface.

---

## ✨ Features

### 1. PDF Resume Upload

Users can upload their resume in PDF format directly through the web application.

### 2. Job Description Selection

The application provides sample job descriptions for:

- Data Analyst
- Data Scientist
- Machine Learning Engineer

Users can also edit or replace the job description with their own requirements.

### 3. Resume–Job Match Score

The system calculates a similarity score between the resume and job description using:

- TF-IDF Vectorization
- Cosine Similarity

The score is calculated dynamically and is not hardcoded.

### 4. Match Categories

The similarity score is interpreted using the following categories:

| Match Score | Category |
|---|---|
| 80–100% | Excellent Match |
| 60–79% | Good Match |
| 40–59% | Moderate Match |
| Below 40% | Low Match |

### 5. Skill Extraction

The application identifies technical and analytical skills from the resume and job description.

Examples include:

- Python
- SQL
- Excel
- Power BI
- Tableau
- Pandas
- NumPy
- Scikit-learn
- Machine Learning
- Deep Learning
- Statistics
- Git
- GitHub
- Docker
- AWS
- Azure
- MongoDB
- MySQL
- PostgreSQL

The system also handles common skill variations such as:

- MS Excel → Excel
- Microsoft Excel → Excel
- Python Scripting → Python
- SQL Querying → SQL
- Statistical Analysis → Statistics
- Exploratory Data Analysis → Data Analysis

### 6. Matching Skills

Skills present in both the resume and job description are displayed as matching skills.

### 7. Missing Skills

Skills required by the job description but not detected in the resume are displayed as missing skills.

### 8. Skill-Based Role Recommendation

The system provides transparent, rule-based recommendations for roles such as:

- Data Scientist
- Data Analyst
- Machine Learning Engineer
- Software Developer
- Web Developer

The role recommendation is based on detected skills and is explicitly rule-based rather than being presented as a trained neural-network prediction.

### 9. Visual Analytics

The application provides visual representations of:

- Matching vs Missing Skills
- Resume–Job Match Score
- Match Gap

### 10. Resume Improvement Suggestions

The system provides suggestions based on missing skills and job requirements.

The system does not instruct candidates to falsely add skills or experience they do not have.

---

## 🧠 Machine Learning Methodology

### TF-IDF

TF-IDF (Term Frequency–Inverse Document Frequency) converts resume and job-description text into numerical vectors.

It gives higher importance to terms that are useful for distinguishing documents while reducing the importance of very common terms.

### Cosine Similarity

Cosine similarity measures the similarity between the resume vector and job-description vector.

The resulting similarity value is converted into a percentage to produce the Resume–Job Match Score.

Formula:

Cosine Similarity =

    A · B
    -------
    |A| |B|

where:

- A = Resume TF-IDF vector
- B = Job Description TF-IDF vector

---

## 🏗️ System Architecture

```text
                 ┌───────────────────────┐
                 │     PDF Resume        │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │   PDF Text Extraction │
                 │       PyMuPDF         │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │ Text Preprocessing    │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │ TF-IDF Vectorization  │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │ Cosine Similarity     │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │ Match Score           │
                 └───────────┬───────────┘
                             │
             ┌───────────────┼────────────────┐
             ▼               ▼                ▼
      Skill Extraction   Missing Skills   Role Analysis
             │               │                │
             └───────────────┼────────────────┘
                             ▼
                 ┌───────────────────────┐
                 │ Results & Charts      │
                 │ Resume Suggestions    │
                 └───────────────────────┘