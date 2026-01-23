import pandas as pd

def run_anomaly(forecast_df, actual_df):

    forecast_df["ds"] = pd.to_datetime(forecast_df["ds"])
    actual_df["date"] = pd.to_datetime(actual_df["date"])

    merged = pd.merge(
        forecast_df,
        actual_df,
        left_on=["ds", "city", "disease"],
        right_on=["date", "city", "disease"],
        how="inner"
    )

    if merged.empty:
        return pd.DataFrame()

    merged["deviation"] = (
        abs(merged["admissions"] - merged["yhat"])
        / merged["yhat"].replace(0, 1)
    )

    def classify(x):
        if x < 0.3:
            return "Normal"
        elif x < 0.6:
            return "Medium"
        else:
            return "High"

    merged["risk"] = merged["deviation"].apply(classify)

    return merged[[
        "date", "city", "disease",
        "admissions", "yhat", "risk"
    ]]
