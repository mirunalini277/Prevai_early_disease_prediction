from ml_pipeline.prediction_model.hospital_weather_model.src.hospital_data_loader import upload_hospital_data
from ml_pipeline.prediction_model.hospital_weather_model.src.weather_api import fetch_weather
from ml_pipeline.prediction_model.hospital_weather_model.src.preprocess import merge_datasets
from ml_pipeline.prediction_model.hospital_weather_model.src.train_model import train_model
from ml_pipeline.prediction_model.hospital_weather_model.src.predict import predict_patients


upload_hospital_data(
    "ml_pipeline/prediction_model/hospital_weather_model/data/raw/hospital_data.csv"
)

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
