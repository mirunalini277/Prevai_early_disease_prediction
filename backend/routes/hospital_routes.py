from fastapi import APIRouter, UploadFile, File
import os
import shutil
import pandas as pd

from backend.ml.ml_engine import run_analysis

router = APIRouter(prefix="/hospital")

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

REQUIRED_COLUMNS = [
    "Date",
    "Region",
    "Diagnosed_Disease",
    "Reported_Cases"
]


@router.post("/upload-csv")
def upload_csv(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        df = pd.read_csv(file_path)
    except Exception:
        return {"status": "error", "message": "Invalid CSV file"}

    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            return {
                "status": "error",
                "message": f"Missing column: {col}"
            }

    analysis_result = run_analysis(file_path)

    return {
        "status": "success",
        "message": "CSV uploaded and processed",
        "analysis_preview": analysis_result
    }
