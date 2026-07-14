import re

import pandas as pd

from app.config import CLEANED_CSV_PATH, JUNIOR_TERMS
from app.salary_parser import parse_salary_range
from app.skill_extractor import extract_skills, skills_to_text


TITLE_MAP = {
    "ai": "AI Engineer",
    "artificial intelligence": "AI Engineer",
    "software": "Software Engineer",
    "frontend": "Software Engineer",
    "backend": "Software Engineer",
    "data analyst": "Data Analyst",
    "machine learning": "Machine Learning Engineer",
    "ml engineer": "Machine Learning Engineer",
    "consultant": "Technology Consultant",
    "business analyst": "Business Analyst",
}


def standardize_title(title: object) -> str:
    text = str(title or "").strip()
    lower = text.lower()
    for keyword, category in TITLE_MAP.items():
        if keyword in lower:
            return category
    return "Other"


def standardize_location(location: object) -> str:
    text = str(location or "Remote").strip()
    lower = text.lower()
    if "remote" in lower:
        return "Remote"
    if "london" in lower:
        return "London"
    if "manchester" in lower:
        return "Manchester"
    if "birmingham" in lower:
        return "Birmingham"
    if "edinburgh" in lower:
        return "Edinburgh"
    if "bristol" in lower:
        return "Bristol"
    if "leeds" in lower:
        return "Leeds"
    return text.title()


def infer_seniority(title: object, description: object) -> str:
    text = f"{title or ''} {description or ''}".lower()
    if any(term in text for term in JUNIOR_TERMS):
        return "Junior/Graduate"
    if re.search(r"\bsenior\b|\blead\b|\bprincipal\b", text):
        return "Senior"
    return "Mid-level"


def clean_jobs(df: pd.DataFrame) -> pd.DataFrame:
    required = {"job_id", "title", "company", "location", "salary", "description", "posted_date"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    cleaned = df.copy()
    cleaned = cleaned.drop_duplicates(subset=["title", "company", "location", "description"])
    cleaned["role_category"] = cleaned["title"].apply(standardize_title)
    cleaned["location_standard"] = cleaned["location"].apply(standardize_location)
    cleaned["seniority"] = cleaned.apply(lambda row: infer_seniority(row["title"], row["description"]), axis=1)
    salaries = cleaned["salary"].apply(parse_salary_range)
    cleaned["salary_min"] = salaries.apply(lambda item: item[0])
    cleaned["salary_max"] = salaries.apply(lambda item: item[1])
    cleaned["salary_avg"] = cleaned[["salary_min", "salary_max"]].mean(axis=1)
    cleaned["skills"] = cleaned["description"].apply(extract_skills)
    cleaned["skills_text"] = cleaned["skills"].apply(skills_to_text)
    cleaned["posted_date"] = pd.to_datetime(cleaned["posted_date"], errors="coerce")
    cleaned = cleaned.dropna(subset=["posted_date"]).reset_index(drop=True)
    return cleaned


def export_cleaned_jobs(df: pd.DataFrame, path=CLEANED_CSV_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    export = df.copy()
    if "skills" in export.columns:
        export["skills"] = export["skills"].apply(lambda value: ";".join(value) if isinstance(value, list) else value)
    export.to_csv(path, index=False)
