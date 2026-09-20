"""Case-insensitive rule-based technical skill extraction."""
import re

SKILL_ALIASES = {
    "Python": ["python"], "Java": ["java"], "C++": ["c++", "cpp"], "SQL": ["sql"],
    "Excel": ["excel", "microsoft excel"], "Power BI": ["power bi", "powerbi"], "Tableau": ["tableau"],
    "Pandas": ["pandas"], "NumPy": ["numpy", "num py"], "Scikit-learn": ["scikit-learn", "scikit learn", "sklearn"],
    "TensorFlow": ["tensorflow"], "PyTorch": ["pytorch"], "Machine Learning": ["machine learning"],
    "Deep Learning": ["deep learning"], "Data Science": ["data science"], "Data Analysis": ["data analysis", "data analytics"],
    "NLP": ["nlp"], "Natural Language Processing": ["natural language processing"], "Computer Vision": ["computer vision"],
    "AWS": ["aws", "amazon web services"], "Azure": ["azure"], "Git": ["git"], "GitHub": ["github"],
    "Docker": ["docker"], "Statistics": ["statistics", "statistical"], "Matplotlib": ["matplotlib"],
    "Seaborn": ["seaborn"], "Keras": ["keras"], "HTML": ["html"], "CSS": ["css"], "JavaScript": ["javascript"],
    "React": ["react", "react.js"], "MongoDB": ["mongodb", "mongo db"], "MySQL": ["mysql"], "PostgreSQL": ["postgresql", "postgres"],
}


def extract_skills(text: str) -> set[str]:
    """Return canonical skill names whose aliases occur as whole terms."""
    found = set()
    lowered = (text or "").lower()
    for skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            pattern = r"(?<![a-z0-9])" + re.escape(alias) + r"(?![a-z0-9])"
            if re.search(pattern, lowered):
                found.add(skill)
                break
    return found
