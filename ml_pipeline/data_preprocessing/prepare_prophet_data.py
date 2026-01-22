import pandas as pd
from data_preprocessing.csv_validator import validate_csv
from data_preprocessing.data_cleaning import clean_data
from data_preprocessing.aggregation import aggregate_data

def prepare_prophet_dataframe(raw_df: pd.DataFrame) -> pd.DataFrame:
    validate_csv(raw_df)

    df = clean_data(raw_df)
    df = aggregate_data(df)

    df = df.rename(columns={
        "Date": "ds",
        "Reported_Cases": "y",
        "Region": "district",
        "Diagnosed_Disease": "disease"
    })

    return df[["ds", "y", "district", "disease"]]
