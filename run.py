from app.cleaning import clean_jobs, export_cleaned_jobs
from app.data_loader import load_raw_jobs
from app.database import save_jobs_to_sqlite


def main() -> None:
    raw = load_raw_jobs()
    cleaned = clean_jobs(raw)
    export_cleaned_jobs(cleaned)
    save_jobs_to_sqlite(cleaned)
    print(f"Prepared {len(cleaned)} cleaned job postings.")
    print("Run the dashboard with: streamlit run app/dashboard.py")


if __name__ == "__main__":
    main()
