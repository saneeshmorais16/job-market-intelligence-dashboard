from app.skill_extractor import extract_skills


def test_extract_known_skills():
    text = "Build Python APIs with FastAPI, Docker, SQL and AWS."
    assert extract_skills(text) == ["Python", "SQL", "FastAPI", "AWS", "Docker"]


def test_extract_ai_ml_variants():
    assert "AI/ML" in extract_skills("Machine learning and LLM evaluation role")
