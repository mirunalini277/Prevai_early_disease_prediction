import pandas as pd
from data_preprocessing.prepare_prophet_data import prepare_prophet_dataframe

def test_prepare_prophet_data():
    raw_df = pd.DataFrame({
        "Date": ["2024-12-01", "2024-12-01"],
        "Region": ["Chennai", "Chennai"],
        "Diagnosed_Disease": ["Dengue", "Dengue"],
        "Reported_Cases": [10, 5]
    })

    result = prepare_prophet_dataframe(raw_df)
    print("\n✅ Final Prophet Data:\n")
    print(result)

if __name__ == "__main__":
    test_prepare_prophet_data()
