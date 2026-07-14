from app.analytics import filter_jobs, junior_graduate_insights, overview_metrics, skill_demand
from app.cleaning import clean_jobs
from app.data_loader import load_raw_jobs


def test_overview_metrics_from_sample_data():
    cleaned = clean_jobs(load_raw_jobs())
    metrics = overview_metrics(cleaned)
    assert metrics["postings"] == 24
    assert metrics["locations"] >= 5


def test_filter_jobs_by_skill_and_seniority():
    cleaned = clean_jobs(load_raw_jobs())
    filtered = filter_jobs(cleaned, seniorities=["Junior/Graduate"], skills=["Python"])
    assert len(filtered) > 0
    assert all(filtered["seniority"] == "Junior/Graduate")


def test_skill_demand_contains_python():
    cleaned = clean_jobs(load_raw_jobs())
    demand = skill_demand(cleaned)
    assert "Python" in demand["skill"].tolist()
    assert int(demand[demand["skill"] == "Python"]["postings"].iloc[0]) > 0


def test_junior_graduate_insights_shape():
    cleaned = clean_jobs(load_raw_jobs())
    insights = junior_graduate_insights(cleaned)
    assert insights["postings"] > 0
    assert len(insights["top_skills"]) <= 5
