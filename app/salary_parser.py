import re
from typing import Optional

import pandas as pd


def parse_salary_range(value: object) -> tuple[Optional[int], Optional[int]]:
    """Parse common UK salary strings into annual min and max values."""
    if pd.isna(value):
        return None, None

    text = str(value).lower().replace(",", "").replace("gbp", "").replace("pounds", "")
    text = text.replace("per annum", "").replace("pa", "").replace("/year", "")
    numbers = re.findall(r"\d+(?:\.\d+)?\s*k?|\d+", text)
    parsed: list[int] = []

    for token in numbers:
        clean = token.strip()
        multiplier = 1000 if clean.endswith("k") else 1
        clean = clean.rstrip("k")
        try:
            amount = int(float(clean) * multiplier)
        except ValueError:
            continue
        if amount < 1000:
            amount *= 1000
        parsed.append(amount)

    if not parsed:
        return None, None
    if len(parsed) == 1:
        return parsed[0], parsed[0]
    return min(parsed[0], parsed[1]), max(parsed[0], parsed[1])
