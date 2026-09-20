"""TF-IDF and cosine-similarity matching."""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .text_processing import preprocess_text


def score_category(score: float) -> str:
    if score >= 80: return "Excellent Match"
    if score >= 60: return "Good Match"
    if score >= 40: return "Moderate Match"
    return "Low Match"


def analyze_match(resume_text: str, job_text: str) -> dict:
    resume = preprocess_text(resume_text)
    job = preprocess_text(job_text)
    if not resume or not job:
        return {"score": 0.0, "category": "Low Match"}
    try:
        vectors = TfidfVectorizer(stop_words="english").fit_transform([resume, job])
        similarity = float(cosine_similarity(vectors[0:1], vectors[1:2])[0][0])
    except ValueError:
        similarity = 0.0
    score = max(0.0, min(100.0, similarity * 100))
    return {"score": score, "category": score_category(score)}
