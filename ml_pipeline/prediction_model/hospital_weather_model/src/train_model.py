import os
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# ----------------------------------
# Resolve project root
# ----------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))

DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "merged_data.csv")
MODEL_DIR = os.path.join(os.path.dirname(__file__), "../models")
MODEL_PATH = os.path.join(MODEL_DIR, "trained_model.pkl")

os.makedirs(MODEL_DIR, exist_ok=True)

# ----------------------------------
# Load data
# ----------------------------------
data = pd.read_csv(DATA_PATH)

# ----------------------------------
# FORCE NUMERIC DATA ONLY
# ----------------------------------
TARGET_COL = "patient_count"

# Drop non-numeric columns safely
numeric_data = data.select_dtypes(include=[np.number])

# Ensure target exists
if TARGET_COL not in numeric_data.columns:
    raise ValueError(f"Target column '{TARGET_COL}' not found in numeric data")

# ----------------------------------
# Handle missing / infinite values
# ----------------------------------
numeric_data = numeric_data.replace([np.inf, -np.inf], np.nan)
numeric_data = numeric_data.fillna(numeric_data.mean())

# ----------------------------------
# Split features & target
# ----------------------------------
X = numeric_data.drop(TARGET_COL, axis=1)
y = numeric_data[TARGET_COL]

# ----------------------------------
# Train-test split
# ----------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------------
# Train model
# ----------------------------------
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# ----------------------------------
# Evaluate
# ----------------------------------
y_pred = model.predict(X_test)
accuracy = r2_score(y_test, y_pred)

print(f"Training completed successfully")
print(f"R2 Score: {accuracy:.2f}")

# ----------------------------------
# Save model
# ----------------------------------
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print(f"Model saved at: {MODEL_PATH}")
