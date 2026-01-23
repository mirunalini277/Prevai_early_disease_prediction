import pandas as pd
from prophet import Prophet

def run_forecast(df):

    results = []

    for (city, disease), data in df.groupby(["city", "disease"]):

        temp = data.rename(columns={
            "date": "ds",
            "admissions": "y"
        }).copy()

        temp["ds"] = pd.to_datetime(temp["ds"])
        temp = temp.sort_values("ds")

        if len(temp) < 7:
            continue

        model = Prophet(
            daily_seasonality=True,
            weekly_seasonality=True
        )
        model.fit(temp[["ds", "y"]])

        future = model.make_future_dataframe(periods=7)
        forecast = model.predict(future)

        next7 = forecast.tail(7)[["ds", "yhat"]]
        next7["city"] = city
        next7["disease"] = disease
        next7["yhat"] = next7["yhat"].round().astype(int)

        results.append(next7)

    return pd.concat(results, ignore_index=True)
