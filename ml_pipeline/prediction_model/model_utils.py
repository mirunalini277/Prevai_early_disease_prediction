import os
import joblib

MODEL_DIR = "ml_pipeline/prediction_model/saved_models"

def ensure_model_dir():
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)

def get_model_path(district, disease):
    filename = f"{district}_{disease}_prophet.pkl".replace(" ", "_")
    return os.path.join(MODEL_DIR, filename)

def save_model(model, district, disease):
    ensure_model_dir()
    path = get_model_path(district, disease)
    joblib.dump(model, path)
    return path

def load_model(district, disease):
    path = get_model_path(district, disease)
    if not os.path.exists(path):
        raise FileNotFoundError("Model not trained yet.")
    return joblib.load(path)
