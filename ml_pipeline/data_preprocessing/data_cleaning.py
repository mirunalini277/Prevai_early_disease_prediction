import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date", "Reported_Cases"])

    df["Reported_Cases"] = df["Reported_Cases"].astype(int)

    return df

