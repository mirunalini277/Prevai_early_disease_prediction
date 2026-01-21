import joblib
import pandas as pd
from config import MODEL_PATH

def predict_patients(weather_input):
    model = joblib.load(MODEL_PATH)

    df = pd.DataFrame([weather_input])
    prediction = model.predict(df)

    print("🔮 Predicted patient count:", int(prediction[0]))
