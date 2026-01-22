import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import mean_absolute_percentage_error
from ml_pipeline.prediction_model.hospital_weather_model.src.config import MODEL_PATH

def risk_level(error_percent):
    if error_percent < 10:
        return "LOW"
    elif error_percent < 25:
        return "MEDIUM"
    return "HIGH"

def run_pipeline():
    df = pd.read_csv("ml_pipeline/prediction_model/hospital_weather_model/data/raw/hospital_data.csv")

    X = df[["temp", "humidity", "pressure", "rain"]]
    y_actual = df["admissions"]

    model = joblib.load(MODEL_PATH)
    y_pred = model.predict(X)

    df["predicted_cases"] = y_pred.astype(int)
    df["error_percent"] = np.abs((y_actual - y_pred) / y_actual) * 100
    df["risk"] = df["error_percent"].apply(risk_level)

    accuracy = 100 - mean_absolute_percentage_error(y_actual, y_pred) * 100

    print("\n📊 ACTUAL VS PREDICTED")
    print(df[["date", "admissions", "predicted_cases", "risk"]])

    print(f"\n🎯 MODEL ACCURACY: {accuracy:.2f}%")

    return {
        "accuracy": accuracy,
        "records": df.to_dict(orient="records")
    }