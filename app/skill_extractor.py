import re

from app.config import SKILLS

SKILL_PATTERNS = {
    "Python": r"\bpython\b",
    "SQL": r"\bsql\b|postgres|mysql|sqlite",
    "AI/ML": r"\bai\b|\bml\b|machine learning|artificial intelligence|llm|nlp",
    "FastAPI": r"\bfastapi\b",
    "React": r"\breact\b|react\.js",
    "AWS": r"\baws\b|amazon web services",
    "Docker": r"\bdocker\b|container",
    "Power BI": r"\bpower\s*bi\b",
    "Tableau": r"\btableau\b",
}


def extract_skills(text: object) -> list[str]:
    if text is None:
        return []
    haystack = str(text).lower()
    found = [skill for skill in SKILLS if re.search(SKILL_PATTERNS[skill], haystack)]
    return found


def skills_to_text(skills: list[str]) -> str:
    return ";".join(skills)
