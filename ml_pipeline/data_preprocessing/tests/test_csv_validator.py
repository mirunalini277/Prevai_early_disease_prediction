import pandas as pd
from data_preprocessing.csv_validator import validate_csv

def test_csv_validator():
    df = pd.DataFrame({
        "Date": ["2024-12-01"],
        "Region": ["Chennai"],
        "Diagnosed_Disease": ["Dengue"],
        "Reported_Cases": [10]
    })

    validate_csv(df)
    print("✅ CSV Validator Passed")

if __name__ == "__main__":
    test_csv_validator()
