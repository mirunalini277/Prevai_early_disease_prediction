import os
import sys
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score

# -------------------------------
# Fix import path
# -------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
sys.path.append(BASE_DIR)

from ml_pipeline.anomaly_detection.risk_classifier import classify_risk

# -------------------------------
# Paths
# -------------------------------
DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "merged_data.csv")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/trained_model.pkl")

TARGET_COL = "patient_count"

# -------------------------------
# Load model
# -------------------------------
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# -------------------------------
# Load & preprocess data
# -------------------------------
data = pd.read_csv(DATA_PATH)

# Numeric only (SAME AS TRAINING)
numeric_data = data.select_dtypes(include=[np.number])

# Replace NaN / inf (SAME AS TRAINING)
numeric_data = numeric_data.replace([np.inf, -np.inf], np.nan)
numeric_data = numeric_data.fillna(numeric_data.mean())

# Split
X = numeric_data.drop(TARGET_COL, axis=1)
y_actual = numeric_data[TARGET_COL]

# -------------------------------
# ALIGN FEATURES WITH TRAINED MODEL
# -------------------------------
X = X[model.feature_names_in_]

# -------------------------------
# Predict
# -------------------------------
y_pred = model.predict(X)

# -------------------------------
# Metrics
# -------------------------------
accuracy = r2_score(y_actual, y_pred)

actual_value = int(y_actual.iloc[-1])
predicted_value = int(y_pred[-1])
from ml_pipeline.anomaly_detection.risk_classifier import classify_single_value
risk = classify_single_value(predicted_value)


# -------------------------------
# OUTPUT
# -------------------------------
print("\n===== MODEL OUTPUT =====")
print(f"Actual Cases    : {actual_value}")
print(f"Predicted Cases : {predicted_value}")
print(f"Accuracy (R2)   : {accuracy:.2f}")
print(f"Risk Level      : {risk}")
print("========================\n")
