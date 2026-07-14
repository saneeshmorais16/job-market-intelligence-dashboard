import pandas as pd

from app.cleaning import clean_jobs


def test_clean_jobs_adds_expected_columns():
    raw = pd.DataFrame(
        [
            {
                "job_id": 1,
                "title": "Graduate AI Engineer",
                "company": "Example",
                "location": "London, UK",
                "salary": "30k - 40k",
                "description": "Python SQL AI role",
                "posted_date": "2026-06-01",
            }
        ]
    )
    cleaned = clean_jobs(raw)
    assert cleaned.loc[0, "role_category"] == "AI Engineer"
    assert cleaned.loc[0, "location_standard"] == "London"
    assert cleaned.loc[0, "seniority"] == "Junior/Graduate"
    assert cleaned.loc[0, "salary_avg"] == 35000
    assert cleaned.loc[0, "skills_text"] == "Python;SQL;AI/ML"


def test_clean_jobs_removes_duplicates():
    raw = pd.DataFrame(
        [
            {
                "job_id": 1,
                "title": "Data Analyst",
                "company": "Example",
                "location": "Remote",
                "salary": "30000 - 35000",
                "description": "SQL Tableau",
                "posted_date": "2026-06-01",
            },
            {
                "job_id": 2,
                "title": "Data Analyst",
                "company": "Example",
                "location": "Remote",
                "salary": "30000 - 35000",
                "description": "SQL Tableau",
                "posted_date": "2026-06-01",
            },
        ]
    )
    assert len(clean_jobs(raw)) == 1
