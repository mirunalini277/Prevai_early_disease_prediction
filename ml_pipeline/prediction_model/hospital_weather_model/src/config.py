# Open-Meteo (NO API KEY REQUIRED)
LATITUDE = 13.08     # Chennai
LONGITUDE = 80.27

OPEN_METEO_URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude={lat}&longitude={lon}"
    "&current_weather=true"
)

RAW_DATA_PATH = "ml_pipeline/prediction_model/hospital_weather_model/data/raw/"
PROCESSED_DATA_PATH = "data/processed/"
MODEL_PATH = "models/trained_model.pkl"
