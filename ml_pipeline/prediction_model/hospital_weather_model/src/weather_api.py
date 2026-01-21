import requests
import pandas as pd
from datetime import datetime
from config import WEATHER_API_KEY, CITY, WEATHER_URL, RAW_DATA_PATH

def fetch_weather():
    params = {
        "q": CITY,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(WEATHER_URL, params=params)
    data = response.json()

    weather_dict = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "rain": data.get("rain", {}).get("1h", 0)
    }

    df = pd.DataFrame([weather_dict])
    df.to_csv(f"{RAW_DATA_PATH}weather_data.csv", index=False)
    print("✅ Weather data saved successfully")
