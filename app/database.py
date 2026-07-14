import sqlite3
from pathlib import Path

import pandas as pd

from app.config import DATABASE_PATH


def save_jobs_to_sqlite(df: pd.DataFrame, db_path: Path = DATABASE_PATH) -> None:
    db_ready = df.copy()
    if "skills" in db_ready.columns:
        db_ready["skills"] = db_ready["skills"].apply(lambda value: ";".join(value) if isinstance(value, list) else value)
    with sqlite3.connect(db_path) as connection:
        db_ready.to_sql("cleaned_jobs", connection, if_exists="replace", index=False)


def load_jobs_from_sqlite(db_path: Path = DATABASE_PATH) -> pd.DataFrame:
    with sqlite3.connect(db_path) as connection:
        return pd.read_sql_query("SELECT * FROM cleaned_jobs", connection)
