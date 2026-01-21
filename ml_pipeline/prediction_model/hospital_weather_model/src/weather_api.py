import requests
import pandas as pd
from datetime import datetime
from .config import OPEN_METEO_URL, LATITUDE, LONGITUDE, RAW_DATA_PATH


def fetch_weather():
    url = OPEN_METEO_URL.format(lat=LATITUDE, lon=LONGITUDE)

    response = requests.get(url)
    data = response.json()

    # Safety check
    if "current_weather" not in data:
        print(" Open-Meteo API error:", data)
        return

    weather = data["current_weather"]

    weather_dict = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "temp": weather["temperature"],
        "humidity": 65,              # Open-Meteo free tier doesn't give humidity
        "pressure": 1013,            # Default standard pressure
        "rain": weather.get("rain", 0)
    }

    df = pd.DataFrame([weather_dict])
    df.to_csv(f"{RAW_DATA_PATH}weather_data.csv", index=False)

    print(" Weather data fetched from Open-Meteo")
