import pandas as pd
from model_utils import load_model

def generate_forecast(district, disease, days=7):
    model = load_model(district, disease)

    future = model.make_future_dataframe(periods=days)

    forecast = model.predict(future)

    result = forecast[["ds", "yhat"]].tail(days)
    result["district"] = district
    result["disease"] = disease
    result.rename(columns={"yhat": "predicted_cases"}, inplace=True)

    return result
