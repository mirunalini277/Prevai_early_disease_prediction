import pandas as pd
from data_preprocessing.data_cleaning import clean_data

def test_data_cleaning():
    df = pd.DataFrame({
        "Date": ["2024-12-01", "invalid"],
        "Reported_Cases": [10, None]
    })

    cleaned = clean_data(df)
    print("\n✅ Cleaned Data:\n")
    print(cleaned)

if __name__ == "__main__":
    test_data_cleaning()
