import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
from pathlib import Path
from .config import PROCESSED_DATA_PATH, MODEL_PATH

def train_model():
    df = pd.read_csv(f"{PROCESSED_DATA_PATH}merged_data.csv")

    X = df[["temp", "humidity", "pressure", "rain"]]
    y = df["patient_count"]

    model = LinearRegression()
    model.fit(X, y)

    # 🔹 Ensure model directory exists
    model_path = Path(MODEL_PATH)
    model_path.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, model_path)
    print(" Model trained & saved successfully")
