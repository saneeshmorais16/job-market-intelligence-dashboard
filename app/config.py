from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
SAMPLE_DATA_PATH = DATA_DIR / "sample_jobs.csv"
CLEANED_DIR = DATA_DIR / "cleaned"
CLEANED_CSV_PATH = CLEANED_DIR / "cleaned_jobs.csv"
DATABASE_PATH = BASE_DIR / "job_market.db"

ROLE_CATEGORIES = [
    "AI Engineer",
    "Software Engineer",
    "Data Analyst",
    "Machine Learning Engineer",
    "Technology Consultant",
    "Business Analyst",
]

SKILLS = [
    "Python",
    "SQL",
    "AI/ML",
    "FastAPI",
    "React",
    "AWS",
    "Docker",
    "Power BI",
    "Tableau",
]

JUNIOR_TERMS = ["junior", "graduate", "entry", "associate", "intern"]
