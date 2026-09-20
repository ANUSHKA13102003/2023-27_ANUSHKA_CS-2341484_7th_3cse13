"""Transparent skill-coverage role recommendations."""
ROLE_SKILLS = {
    "Data Scientist": ["Python", "Machine Learning", "Pandas", "NumPy", "Statistics", "Scikit-learn", "Data Science"],
    "Data Analyst": ["Python", "SQL", "Excel", "Power BI", "Tableau", "Data Analysis", "Pandas"],
    "Machine Learning Engineer": ["Python", "Machine Learning", "TensorFlow", "PyTorch", "Scikit-learn", "Git", "Docker"],
    "Software Developer": ["Python", "Java", "C++", "SQL", "Git"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React"],
}


def recommend_roles(candidate_skills: set[str]) -> list[dict]:
    results = []
    for role, required in ROLE_SKILLS.items():
        detected = [skill for skill in required if skill in candidate_skills]
        results.append({"role": role, "percentage": round(len(detected) / len(required) * 100, 1), "detected": ", ".join(detected) or "None", "required": ", ".join(required)})
    return sorted(results, key=lambda item: item["percentage"], reverse=True)
