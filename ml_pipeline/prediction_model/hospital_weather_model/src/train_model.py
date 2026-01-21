import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
from config import PROCESSED_DATA_PATH, MODEL_PATH

def train_model():
    df = pd.read_csv(f"{PROCESSED_DATA_PATH}merged_data.csv")

    X = df[["temp","humidity","pressure","rain"]]
    y = df["patient_count"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)
    print("✅ Model trained & saved")
