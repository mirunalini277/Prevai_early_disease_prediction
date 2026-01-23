from backend.ml.forecast import run_forecast
from backend.ml.anomaly import run_anomaly

def run_pipeline():
    run_forecast()
    run_anomaly()
