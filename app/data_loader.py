from pathlib import Path

import pandas as pd

from app.config import SAMPLE_DATA_PATH


def load_raw_jobs(path: Path = SAMPLE_DATA_PATH) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Sample dataset not found: {path}")
    return pd.read_csv(path)
