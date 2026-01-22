import pandas as pd

def aggregate_data(df: pd.DataFrame) -> pd.DataFrame:
    aggregated = (
        df.groupby(["Date", "Region", "Diagnosed_Disease"], as_index=False)
        .agg({"Reported_Cases": "sum"})
    )

    return aggregated
