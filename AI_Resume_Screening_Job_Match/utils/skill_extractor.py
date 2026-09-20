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


def _normalize_alias(alias: str) -> str:
    """Normalize punctuation so variants like 'machine-learning' behave like 'machine learning'."""
    return re.sub(r"[^a-z0-9]+", " ", (alias or "").lower()).strip()


def extract_skills(text: str) -> set[str]:
    """Return canonical skill names whose aliases occur as whole terms."""
    found = set()
    lowered = (text or "").lower()
    normalized_text = re.sub(r"[^a-z0-9]+", " ", lowered).strip()

    for skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            alias_norm = _normalize_alias(alias)
            if not alias_norm:
                continue
            pattern = r"(?<![a-z0-9])" + re.escape(alias_norm).replace(r"\ ", r"\s+") + r"(?![a-z0-9])"
            if re.search(pattern, normalized_text):
                found.add(skill)
                break
    return found
