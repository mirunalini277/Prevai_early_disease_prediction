import pandas as pd
from prophet import Prophet
from model_utils import save_model

def train_model(df, location, disease):
    """
    df must contain: date, reported_cases, location, disease
    """

    # filter data
    df_filtered = df[
        (df["location"] == location) &
        (df["disease"] == disease)
    ]

    if len(df_filtered) < 10:
        raise ValueError("Not enough data to train model")

    # convert to Prophet format
    data = df_filtered[["date", "reported_cases"]].rename(
        columns={
            "date": "ds",
            "reported_cases": "y"
        }
    )

    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False
    )

    model.fit(data)

    model_path = save_model(model, location, disease)
    print(f"✅ Model trained & saved at {model_path}")

    return model
