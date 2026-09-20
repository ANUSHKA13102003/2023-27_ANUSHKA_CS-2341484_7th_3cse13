from utils.skill_extractor import extract_skills


def test_extract_skills_accepts_common_resume_variants():
    text = (
        "Experienced in machine-learning, power bi, scikit learn, num-py, "
        "deep learning, mysql, and natural language processing."
    )
    skills = extract_skills(text)

    assert "Machine Learning" in skills
    assert "Power BI" in skills
    assert "Scikit-learn" in skills
    assert "NumPy" in skills
    assert "Deep Learning" in skills
    assert "MySQL" in skills
    assert "Natural Language Processing" in skills


def test_extract_skills_ignores_partial_word_matches():
    assert "Git" in extract_skills("GitHub and Git are used daily")
    assert "Git" in extract_skills("This project uses git version control")
