import pandas as pd
from pathlib import Path
from .config import RAW_DATA_PATH, PROCESSED_DATA_PATH

def merge_datasets():
    hospital_df = pd.read_csv(f"{RAW_DATA_PATH}hospital_data.csv")
    weather_df = pd.read_csv(f"{RAW_DATA_PATH}weather_data.csv")

    # 🔹 Take the latest weather row
    latest_weather = weather_df.iloc[0]

    # 🔹 Broadcast weather to all hospital rows
    for col in ["temp", "humidity", "pressure", "rain"]:
        hospital_df[col] = latest_weather[col]

    # 🔹 Standardize target column
    if "admissions" in hospital_df.columns:
        hospital_df = hospital_df.rename(columns={"admissions": "patient_count"})

    processed_dir = Path(PROCESSED_DATA_PATH)
    processed_dir.mkdir(parents=True, exist_ok=True)

    hospital_df.to_csv(processed_dir / "merged_data.csv", index=False)

    print("✅ Datasets merged successfully (weather broadcasted)")
