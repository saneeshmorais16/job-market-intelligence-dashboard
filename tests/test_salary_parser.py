from app.salary_parser import parse_salary_range


def test_parse_salary_range_with_k_values():
    assert parse_salary_range("30k - 45k") == (30000, 45000)


def test_parse_salary_range_with_gbp_words():
    assert parse_salary_range("GBP 50000 to GBP 65000") == (50000, 65000)


def test_parse_salary_range_missing_value():
    assert parse_salary_range("") == (None, None)
