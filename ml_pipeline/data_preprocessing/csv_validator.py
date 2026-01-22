import pandas as pd

REQUIRED_COLUMNS = {
    "Date",
    "Region",
    "Diagnosed_Disease",
    "Reported_Cases"
}

def validate_csv(df: pd.DataFrame):
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
