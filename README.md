# Job Market Intelligence Dashboard

A portfolio-ready Streamlit dashboard that analyses safe sample job posting data across skills demand, salary ranges, locations, role categories, seniority and junior/graduate hiring patterns.

## What This Project Does

The project loads a realistic fake job posting dataset, cleans it, extracts useful features, stores the cleaned result in SQLite and presents interactive market insights in a dashboard.

## Why It Matters

Job seekers and early-career technologists need a simple way to understand which skills, locations and role types appear most often in job postings. This project demonstrates practical data cleaning, analysis, dashboarding and testing without using private or scraped data.

## Problem Statement

Raw job posting data is often inconsistent: titles vary, salary text is messy, locations are formatted differently and skills are buried in descriptions. This dashboard turns that messy input into structured insights.

## Tech Stack

- Python
- pandas and NumPy
- Streamlit
- Plotly
- SQLite and SQL
- pytest
- GitHub Actions

## Core Features

- Safe sample job posting dataset
- Data cleaning pipeline
- Duplicate removal
- Job title, location and seniority standardisation
- Salary range parsing
- Skill extraction from descriptions
- SQLite storage for cleaned jobs
- Cleaned CSV export
- Dashboard filters for location, role, seniority, skill and salary range
- Literal skill filtering so terms such as `C++` and `AI/ML` behave correctly
- Automated tests and CI workflow

## Dashboard Sections

- Overview
- Top skills
- Role categories
- Salary insights
- Location trends
- Junior/graduate role analysis

## Example Insights

- Python, SQL and AI/ML are common across technical and analytics roles in the sample data.
- Junior and graduate roles often ask for Python or SQL foundations plus communication skills.
- Remote, London and Manchester appear frequently in the sample dataset.

## Setup

```bash
pip install -r requirements.txt
```

## Prepare Data

```bash
python run.py
```

This creates a local SQLite database and a cleaned CSV export. These generated files are ignored by Git.

## Run The Dashboard

```bash
streamlit run app/dashboard.py
```

## Run Tests

```bash
pytest
```

## Screenshots

Screenshots can be added after running the dashboard locally. Do not commit private data, local exports or generated packets.

## Data Ethics And Limitations

This project uses realistic fake job postings for demonstration. It does not scrape job boards, does not include private data and does not claim real-time market coverage. Insights are only representative of the bundled sample dataset.

## Future Improvements

- Add optional ingestion for explicitly licensed public datasets.
- Add time-series trend views.
- Add more robust natural language skill extraction.
- Add downloadable chart images.
- Add dashboard screenshots after local review.

## No-Secrets Note

Do not commit `.env` files, API keys, tokens, credentials, passwords, private data, scraped data, databases, logs, generated PDFs, application packets or exports.
