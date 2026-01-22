import pandas as pd
from data_preprocessing.aggregation import aggregate_data

def test_aggregation():
    df = pd.DataFrame({
        "Date": ["2024-12-01", "2024-12-01"],
        "Region": ["Chennai", "Chennai"],
        "Diagnosed_Disease": ["Dengue", "Dengue"],
        "Reported_Cases": [10, 5]
    })

    aggregated = aggregate_data(df)
    print("\n✅ Aggregated Data:\n")
    print(aggregated)

if __name__ == "__main__":
    test_aggregation()
