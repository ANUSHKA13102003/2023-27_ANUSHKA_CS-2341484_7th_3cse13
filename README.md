# AI Resume Screening & Job Match System

An interactive Data Science and Machine Learning web application that analyzes a candidate's resume against a job description using Natural Language Processing (NLP).

## 🌐 Live Demo

**Try the application:**  
https://anushka13102003-2023-27-ai-resume-screening-job-matchapp-a1xzq.streamlit.app

## 📌 Project Overview

The **AI Resume Screening & Job Match System** automates the initial comparison between a candidate's resume and a job description.

The application accepts a PDF resume, extracts its text, processes the content using NLP techniques, and calculates a resume-to-job similarity score using **TF-IDF and Cosine Similarity**.

It also identifies:

- Candidate skills
- Matching skills
- Missing skills
- Skill-based role recommendations
- Resume improvement suggestions
- Visual match analysis

## 🔄 System Workflow

```text
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
Matching / Missing Skills
    ↓
Role Recommendation
    ↓
Results & Visualizations