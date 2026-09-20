from utils.skill_extractor import extract_skills


def test_extract_skills_accepts_common_resume_variants():
    text = (
        "Experienced in machine-learning, power bi, scikit learn, num-py, "
        "deep learning, mysql, microsoft excel, statistical analysis, "
        "exploratory data analysis, sql querying, python scripting, "
        "data visualization, data cleaning, data validation, git hub, "
        "natural language processing, and mongo db."
    )
    skills = extract_skills(text)

    assert "Machine Learning" in skills
    assert "Power BI" in skills
    assert "Scikit-learn" in skills
    assert "NumPy" in skills
    assert "Deep Learning" in skills
    assert "MySQL" in skills
    assert "Excel" in skills
    assert "Statistics" in skills
    assert "Data Analysis" in skills
    assert "SQL" in skills
    assert "Python" in skills
    assert "Data Visualization" in skills
    assert "Data Cleaning" in skills
    assert "Data Validation" in skills
    assert "GitHub" in skills
    assert "Natural Language Processing" in skills
    assert "MongoDB" in skills


def test_extract_skills_ignores_partial_word_matches():
    assert "Git" in extract_skills("GitHub and Git are used daily")
    assert "Git" in extract_skills("This project uses git version control")
    assert "SQL" in extract_skills("SQL querying and SQL query development")
    assert "Excel" in extract_skills("MS Excel and Microsoft Excel are used")
    assert "Statistics" in extract_skills("Statistical analysis and statistical methods")
