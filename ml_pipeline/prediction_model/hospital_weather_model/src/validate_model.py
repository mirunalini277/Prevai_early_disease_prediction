import pandas as pd
import joblib
from .config import PROCESSED_DATA_PATH, MODEL_PATH


def validate_model():
    print(" Loading trained model...")
    model = joblib.load(MODEL_PATH)

    print(" Loading processed data...")
    df = pd.read_csv(f"{PROCESSED_DATA_PATH}merged_data.csv")

    X = df[["temp", "humidity", "pressure", "rain"]]

    print(" Running prediction on sample data...")
    preds = model.predict(X.head(5))

    print(" Model validation successful")
    print("Sample predictions:")
    print(preds)


if __name__ == "__main__":
    validate_model()
