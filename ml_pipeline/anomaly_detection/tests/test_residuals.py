import pandas as pd
from anomaly_detection.residual import calculate_residuals

def test_residuals():
    actual_df = pd.DataFrame({
        "date": ["2024-12-01", "2024-12-08"],
        "district": ["Chennai", "Chennai"],
        "disease": ["Dengue", "Dengue"],
        "actual_cases": [10, 30]
    })

    predicted_df = pd.DataFrame({
        "date": ["2024-12-01", "2024-12-08"],
        "district": ["Chennai", "Chennai"],
        "disease": ["Dengue", "Dengue"],
        "predicted_cases": [12, 20]
    })

    result = calculate_residuals(actual_df, predicted_df)
    print("\n✅ Residuals Output:\n", result)

if __name__ == "__main__":
    test_residuals()
