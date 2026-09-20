"""Case-insensitive rule-based technical skill extraction."""
import re

SKILL_ALIASES = {
    "Python": ["python", "python scripting"],
    "Java": ["java"],
    "C++": ["c++", "cpp"],
    "SQL": ["sql", "sql querying", "sql query development", "sql queries", "sql query writing"],
    "Excel": ["excel", "ms excel", "microsoft excel", "microsoft office excel"],
    "Power BI": ["power bi", "powerbi", "power-bi"],
    "Tableau": ["tableau"],
    "Pandas": ["pandas"],
    "NumPy": ["numpy", "num py", "num-py"],
    "Scikit-learn": ["scikit-learn", "scikit learn", "sklearn"],
    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch"],
    "Machine Learning": ["machine learning", "machine-learning", "ml"],
    "Deep Learning": ["deep learning", "deep-learning"],
    "Data Science": ["data science"],
    "Data Analysis": ["data analysis", "exploratory data analysis", "eda", "data analytics"],
    "Data Visualization": ["data visualization", "data visualisation"],
    "Data Cleaning": ["data cleaning", "data cleansing"],
    "Data Validation": ["data validation", "data quality validation"],
    "NLP": ["nlp"],
    "Natural Language Processing": ["natural language processing", "natural-language-processing"],
    "Computer Vision": ["computer vision", "computer-vision"],
    "AWS": ["aws", "amazon web services"],
    "Azure": ["azure"],
    "Git": ["git"],
    "GitHub": ["github", "git hub"],
    "Docker": ["docker"],
    "Statistics": ["statistics", "statistical analysis", "statistical methods", "statistical methods and inference"],
    "Matplotlib": ["matplotlib"],
    "Seaborn": ["seaborn"],
    "Keras": ["keras"],
    "HTML": ["html"],
    "CSS": ["css"],
    "JavaScript": ["javascript", "js"],
    "React": ["react", "react.js", "react js"],
    "MongoDB": ["mongodb", "mongo db", "mongo-db"],
    "MySQL": ["mysql", "my sql", "my-sql"],
    "PostgreSQL": ["postgresql", "postgres", "postgre sql"],
}


def _normalize_alias(alias: str) -> str:
    """Normalize punctuation, spacing, and common separator variants so they behave as a single skill token."""
    return re.sub(r"[^a-z0-9]+", " ", (alias or "").lower()).strip()


def extract_skills(text: str) -> set[str]:
    """Return canonical skill names whose aliases occur as whole terms."""
    found = set()
    if not text:
        return found

    normalized_text = re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()

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
