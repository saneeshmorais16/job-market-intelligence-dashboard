import plotly.express as px
import streamlit as st

from app.analytics import (
    filter_jobs,
    junior_graduate_insights,
    overview_metrics,
    role_category_counts,
    salary_by_location,
    salary_by_role,
    skill_demand,
)
from app.cleaning import clean_jobs, export_cleaned_jobs
from app.config import CLEANED_CSV_PATH
from app.data_loader import load_raw_jobs
from app.database import save_jobs_to_sqlite


@st.cache_data
def load_dashboard_data():
    raw = load_raw_jobs()
    cleaned = clean_jobs(raw)
    export_cleaned_jobs(cleaned)
    save_jobs_to_sqlite(cleaned)
    return cleaned


def render_metric_cards(metrics):
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Postings", metrics["postings"])
    col2.metric("Average salary", f"GBP {metrics['avg_salary']:,.0f}")
    col3.metric("Locations", metrics["locations"])
    col4.metric("Role categories", metrics["role_categories"])


def main():
    st.set_page_config(page_title="Job Market Intelligence Dashboard", layout="wide")
    st.title("Job Market Intelligence Dashboard")
    st.caption("Safe sample dataset for portfolio analysis. No scraping, private data or real-time market coverage.")

    df = load_dashboard_data()

    st.sidebar.header("Filters")
    locations = st.sidebar.multiselect("Location", sorted(df["location_standard"].unique()))
    role_types = st.sidebar.multiselect("Role type", sorted(df["role_category"].unique()))
    seniorities = st.sidebar.multiselect("Seniority", sorted(df["seniority"].unique()))
    all_skills = sorted({skill for skills in df["skills"] for skill in skills})
    selected_skills = st.sidebar.multiselect("Skill", all_skills)
    salary_min = int(df["salary_avg"].min())
    salary_max = int(df["salary_avg"].max())
    salary_range = st.sidebar.slider("Average salary range", salary_min, salary_max, (salary_min, salary_max), step=1000)

    filtered = filter_jobs(df, locations, role_types, seniorities, selected_skills, salary_range)
    render_metric_cards(overview_metrics(filtered))

    tab_overview, tab_skills, tab_roles, tab_salary, tab_locations, tab_junior = st.tabs(
        ["Overview", "Top skills", "Role categories", "Salary insights", "Location trends", "Junior/graduate"]
    )

    with tab_overview:
        st.subheader("Filtered job postings")
        st.dataframe(
            filtered[["title", "company", "location_standard", "role_category", "seniority", "salary_avg", "skills_text"]],
            use_container_width=True,
        )
        with open(CLEANED_CSV_PATH, "rb") as file:
            st.download_button("Download cleaned CSV", file, file_name="cleaned_jobs.csv", mime="text/csv")

    with tab_skills:
        skills_df = skill_demand(filtered)
        st.plotly_chart(px.bar(skills_df, x="skill", y="postings", title="Skills demand"), use_container_width=True)

    with tab_roles:
        role_df = role_category_counts(filtered)
        st.plotly_chart(px.bar(role_df, x="role_category", y="postings", title="Postings by role category"), use_container_width=True)

    with tab_salary:
        salary_role = salary_by_role(filtered)
        salary_location = salary_by_location(filtered)
        st.plotly_chart(px.bar(salary_role, x="role_category", y="avg_salary", title="Average salary by role"), use_container_width=True)
        st.plotly_chart(px.bar(salary_location, x="location_standard", y="avg_salary", title="Average salary by location"), use_container_width=True)

    with tab_locations:
        location_df = salary_by_location(filtered)
        st.plotly_chart(px.bar(location_df, x="location_standard", y="postings", title="Posting volume by location"), use_container_width=True)

    with tab_junior:
        insights = junior_graduate_insights(filtered)
        st.metric("Junior/graduate postings", insights["postings"])
        st.subheader("Most requested skills")
        st.dataframe(insights["top_skills"], use_container_width=True)
        st.subheader("Best-fit role categories")
        st.dataframe(insights["best_fit_roles"], use_container_width=True)
        st.subheader("Common requirements")
        st.write(", ".join(insights["common_requirements"]))


if __name__ == "__main__":
    main()
