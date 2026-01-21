from src.hospital_data_loader import upload_hospital_data
from src.weather_api import fetch_weather
from src.preprocess import merge_datasets
from src.train_model import train_model
from src.predict import predict_patients

upload_hospital_data("hospital_data.csv")
fetch_weather()
merge_datasets()
train_model()

new_weather = {
    "temp": 32,
    "humidity": 65,
    "pressure": 1012,
    "rain": 0
}

predict_patients(new_weather)
