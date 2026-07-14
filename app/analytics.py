import pandas as pd

from app.config import ROLE_CATEGORIES, SKILLS


def filter_jobs(
    df: pd.DataFrame,
    locations: list[str] | None = None,
    role_types: list[str] | None = None,
    seniorities: list[str] | None = None,
    skills: list[str] | None = None,
    salary_range: tuple[int, int] | None = None,
) -> pd.DataFrame:
    filtered = df.copy()
    if locations:
        filtered = filtered[filtered["location_standard"].isin(locations)]
    if role_types:
        filtered = filtered[filtered["role_category"].isin(role_types)]
    if seniorities:
        filtered = filtered[filtered["seniority"].isin(seniorities)]
    if skills:
        pattern = "|".join(skills)
        filtered = filtered[filtered["skills_text"].str.contains(pattern, case=False, na=False)]
    if salary_range:
        low, high = salary_range
        filtered = filtered[(filtered["salary_avg"] >= low) & (filtered["salary_avg"] <= high)]
    return filtered


def overview_metrics(df: pd.DataFrame) -> dict[str, float]:
    return {
        "postings": int(len(df)),
        "avg_salary": round(float(df["salary_avg"].dropna().mean()), 2) if not df.empty else 0,
        "locations": int(df["location_standard"].nunique()) if not df.empty else 0,
        "role_categories": int(df["role_category"].nunique()) if not df.empty else 0,
    }


def skill_demand(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for skill in SKILLS:
        count = int(df["skills_text"].str.contains(skill, case=False, regex=False, na=False).sum())
        rows.append({"skill": skill, "postings": count})
    return pd.DataFrame(rows).sort_values("postings", ascending=False)


def role_category_counts(df: pd.DataFrame) -> pd.DataFrame:
    counts = df["role_category"].value_counts().reindex(ROLE_CATEGORIES, fill_value=0)
    return (
        counts.rename_axis("role_category")
        .reset_index(name="postings")
        .sort_values("postings", ascending=False)
    )


def salary_by_role(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("role_category", as_index=False)
        .agg(avg_salary=("salary_avg", "mean"), min_salary=("salary_min", "mean"), max_salary=("salary_max", "mean"))
        .round(2)
        .sort_values("avg_salary", ascending=False)
    )


def salary_by_location(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("location_standard", as_index=False)
        .agg(avg_salary=("salary_avg", "mean"), postings=("job_id", "count"))
        .round(2)
        .sort_values("avg_salary", ascending=False)
    )


def junior_graduate_insights(df: pd.DataFrame) -> dict[str, object]:
    junior = df[df["seniority"] == "Junior/Graduate"]
    return {
        "postings": int(len(junior)),
        "top_skills": skill_demand(junior).head(5).to_dict(orient="records"),
        "best_fit_roles": role_category_counts(junior).head(5).to_dict(orient="records"),
        "common_requirements": [
            "portfolio projects",
            "Python or SQL foundations",
            "clear communication",
            "data analysis or software delivery basics",
        ],
    }
