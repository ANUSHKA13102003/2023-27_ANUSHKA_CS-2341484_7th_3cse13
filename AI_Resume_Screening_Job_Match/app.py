"""Streamlit dashboard for AI Resume Screening and Job Matching."""
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

from utils.matcher import analyze_match
from utils.pdf_extractor import extract_text_from_pdf
from utils.role_recommender import recommend_roles
from utils.skill_extractor import extract_skills

PROJECT_DIR = Path(__file__).parent

SAMPLE_JOBS = {
    "Data Scientist": """We are looking for a Data Scientist with Python, Pandas, NumPy, SQL, statistics, data analysis, machine learning, and scikit-learn experience. The candidate should communicate insights and build reliable predictive models.""",
    "Data Analyst": """We need a Data Analyst skilled in SQL, Excel, Python, Pandas, data analysis, Power BI, Tableau, and statistics. Responsibilities include dashboards, reporting, data cleaning, and communicating business insights.""",
    "Machine Learning Engineer": """Seeking a Machine Learning Engineer experienced with Python, machine learning, scikit-learn, TensorFlow or PyTorch, Git, Docker, model evaluation, and production-minded software practices.""",
}
DEMO_RESUME = """Anushka\nB.Tech Computer Science\nData Science and Machine Learning Internship\nSkills: Python, SQL, Pandas, NumPy, Machine Learning, Scikit-learn, Matplotlib, Git, Data Analysis\nProjects: Student Performance Prediction; Customer Churn Prediction; Sales Data Analysis"""

st.set_page_config(page_title="AI Resume Screening", page_icon="📄", layout="wide")
st.markdown("""<style>
.block-container {padding-top: 2rem; padding-bottom: 2rem;}
[data-testid="stMetric"] {
    background: linear-gradient(180deg, #1f2937 0%, #111827 100%);
    border: 1px solid rgba(148, 163, 184, 0.35);
    border-radius: 12px;
    padding: 1rem 1.1rem;
    box-shadow: 0 6px 14px rgba(15, 23, 42, 0.22);
}
[data-testid="stMetric"] > div {
    background: transparent !important;
}
[data-testid="stMetric"] label {
    color: #dbeafe !important;
    font-weight: 600;
    letter-spacing: 0.02em;
}
[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #f8fafc !important;
    font-weight: 700;
    font-size: 1.8rem !important;
}
</style>""", unsafe_allow_html=True)

st.title("📄 AI Resume Screening & Job Match System")
st.caption("A transparent, local NLP dashboard for resume-to-job comparison")
st.info("This university project uses TF-IDF and cosine similarity for text matching, plus explainable rule-based skill and role analysis.")

with st.sidebar:
    st.header("Analysis Settings")
    demo_mode = st.toggle("Demo Mode", value=True, help="Use clearly labelled sample candidate data without uploading a PDF.")
    selected_role = st.selectbox("Sample job description", list(SAMPLE_JOBS))
    st.markdown("---")
    st.markdown("**Pipeline**")
    st.write("PDF → text extraction → preprocessing → TF-IDF → cosine similarity → skills → recommendations")
    st.caption("No paid API or API key is used.")

left, right = st.columns([1, 1])
with left:
    st.subheader("1. Candidate Resume")
    uploaded_file = st.file_uploader("Upload a PDF resume", type=["pdf"])
    if demo_mode:
        st.success("Demo Candidate — For Demonstration Purposes Only")
        st.write("**Anushka** · B.Tech Computer Science")
        st.caption("Demo data: Python, SQL, Pandas, NumPy, Machine Learning, Scikit-learn, Matplotlib, Git, Data Analysis")
    elif not uploaded_file:
        st.warning("Upload a readable PDF or enable Demo Mode to continue.")

with right:
    st.subheader("2. Job Description")
    job_description = st.text_area("Edit or replace the job description", value=SAMPLE_JOBS[selected_role], height=180)
    analyze_clicked = st.button("🔍 Analyze Resume", type="primary", use_container_width=True)

if analyze_clicked or demo_mode:
    with st.spinner("Analyzing resume and job description..."):
        if demo_mode:
            resume_text = DEMO_RESUME
            source_label = "Demo Candidate"
        elif uploaded_file:
            try:
                resume_text = extract_text_from_pdf(uploaded_file)
                source_label = uploaded_file.name
            except ValueError as exc:
                st.error(str(exc))
                st.stop()
        else:
            st.error("Please upload a PDF resume or enable Demo Mode.")
            st.stop()

        if not job_description.strip():
            st.error("Please enter a non-empty job description.")
            st.stop()
        if len(resume_text.split()) < 5:
            st.warning("Very little readable resume text was found; results may not be meaningful.")

        result = analyze_match(resume_text, job_description)
        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_description)
        matching = sorted(resume_skills & job_skills)
        missing = sorted(job_skills - resume_skills)
        recommendations = recommend_roles(resume_skills)

    st.markdown(f"### Results · `{source_label}`")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Resume–Job Match", f"{result['score']:.1f}%")
    m2.metric("Match Category", result["category"])
    m3.metric("Candidate Skills", len(resume_skills))
    m4.metric("Matching Skills", len(matching))

    chart1, chart2 = st.columns(2)
    with chart1:
        fig = px.pie(names=["Match", "Gap"], values=[result["score"], 100 - result["score"]], hole=0.62,
                     title="Resume–Job Match Score", color_discrete_sequence=["#2563eb", "#dbeafe"])
        fig.update_layout(showlegend=True, margin=dict(t=55, b=10, l=10, r=10))
        st.plotly_chart(fig, use_container_width=True)
    with chart2:
        skill_df = pd.DataFrame({"Skill status": ["Matching Skills", "Missing Skills"], "Count": [len(matching), len(missing)]})
        fig = px.bar(skill_df, x="Skill status", y="Count", title="Matching Skills vs Missing Skills",
                     color="Skill status", color_discrete_sequence=["#16a34a", "#f97316"])
        fig.update_layout(showlegend=False, margin=dict(t=55, b=10, l=10, r=10))
        st.plotly_chart(fig, use_container_width=True)

    s1, s2, s3 = st.columns(3)
    with s1:
        st.subheader("Candidate Skills")
        st.write(", ".join(sorted(resume_skills)) if resume_skills else "No predefined technical skills detected.")
    with s2:
        st.subheader("Matching Skills")
        st.write(", ".join(matching) if matching else "No matching skills detected.")
    with s3:
        st.subheader("Missing Skills")
        st.write(", ".join(missing) if missing else "No job-description skills are missing.")

    st.subheader("Skill-Based Role Recommendation")
    st.caption("Transparent rule-based recommendations—not a trained AI model. Percentages show required role skills detected in the candidate data.")
    if recommendations:
        rec_df = pd.DataFrame(recommendations)
        st.dataframe(rec_df.rename(columns={"role": "Role", "percentage": "Coverage %", "detected": "Detected Skills", "required": "Required Skills"}), use_container_width=True, hide_index=True)
    else:
        st.info("No predefined role skills were detected yet.")

    st.subheader("Resume Improvement Suggestions")
    if missing:
        for skill in missing:
            st.write(f"• Consider strengthening **{skill}** with relevant learning or project evidence, if applicable.")
    else:
        st.success("No skill-gap suggestions for this job description. Continue adding measurable evidence to relevant experience.")
    st.caption("Suggestions never ask candidates to claim skills or experience they do not have.")

with st.expander("Technical Methodology", expanded=False):
    st.markdown("""1. **Extract:** PyMuPDF reads text from every PDF page.
2. **Preprocess:** Text is lowercased, punctuation is removed, and whitespace is normalized.
3. **Vectorize:** `TfidfVectorizer` represents important words as numerical vectors.
4. **Compare:** cosine similarity measures the angle between resume and job vectors.
5. **Score:** similarity × 100 is the displayed percentage; category thresholds are configurable in `utils/matcher.py`.
6. **Explain:** a predefined, case-insensitive skill dictionary finds candidate, matching, and missing skills.
7. **Recommend:** role coverage is calculated from detected skills using transparent rules.""")

st.markdown("---")
st.caption("AI Resume Screening & Job Match System · B.Tech Computer Science Internship Project · Runs locally with open-source Python packages")
