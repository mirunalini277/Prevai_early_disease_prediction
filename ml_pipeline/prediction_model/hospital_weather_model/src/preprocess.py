import pandas as pd
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH

def merge_datasets():
    hospital = pd.read_csv(f"{RAW_DATA_PATH}hospital_data.csv")
    weather = pd.read_csv(f"{RAW_DATA_PATH}weather_data.csv")

    merged = pd.merge(hospital, weather, on="date")

    merged.to_csv(f"{PROCESSED_DATA_PATH}merged_data.csv", index=False)
    print("✅ Datasets merged successfully")
