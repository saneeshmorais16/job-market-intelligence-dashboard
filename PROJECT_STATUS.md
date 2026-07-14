# Project Status

## Current Build Status

Working starter version built for local portfolio review. The dashboard runs from a safe sample CSV dataset and does not require external APIs.

## Completed Features

- Safe fake job posting dataset
- Data loading module
- Data cleaning pipeline
- Duplicate removal
- Standardised titles, locations and seniority
- Salary range parsing
- Skill extraction
- SQLite storage for cleaned jobs
- Cleaned CSV export
- Streamlit dashboard with six sections
- Interactive filters
- pytest test suite
- GitHub Actions test workflow
- README and no-secrets guidance

## Remaining Improvements

- Add reviewed dashboard screenshots.
- Add optional licensed public dataset import.
- Add trend analysis by posting date.
- Improve skill extraction with richer taxonomy matching.
- Add accessibility review for dashboard charts.

## Testing Status

Tests cover salary parsing, skill extraction, data cleaning and dashboard data functions. Run:

```bash
pytest
```

## What Must Be Checked Before Making Public

- No `.env` files or credentials are present.
- No real scraped job data is present.
- No database files, exports or logs are committed.
- README does not claim real-time coverage or production usage.
- Dashboard screenshots do not expose private data.

## Files That Must Never Be Committed

- `.env` or `.env.*`
- API keys, tokens, credentials or passwords
- `*.db`, `*.sqlite`, `*.sqlite3`
- logs
- generated PDFs
- application packets
- generated outputs
- private data
- scraped data
- exports
