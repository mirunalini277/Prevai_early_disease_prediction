import pandas as pd
from residual import calculate_residuals

# Step 1: Create dummy ACTUAL data
actual_data = {
    "date": ["2024-12-01", "2024-12-08"],
    "district": ["Chennai", "Chennai"],
    "disease": ["Dengue", "Dengue"],
    "actual_cases": [10, 30]
}

actual_df = pd.DataFrame(actual_data)

# Step 2: Create dummy PREDICTED data
predicted_data = {
    "date": ["2024-12-01", "2024-12-08"],
    "district": ["Chennai", "Chennai"],
    "disease": ["Dengue", "Dengue"],
    "predicted_cases": [12, 20]
}

predicted_df = pd.DataFrame(predicted_data)

# Step 3: Run residual calculation
result_df = calculate_residuals(actual_df, predicted_df)

# Step 4: Print result
print("\n✅ Residuals Output:\n")
print(result_df)
