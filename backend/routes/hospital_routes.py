from fastapi import APIRouter, UploadFile, File, Depends
import pandas as pd
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.models import HospitalRecord
from backend.ml.ml_engine import run_analysis

router = APIRouter(prefix="/hospital")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload-csv")
def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    df = pd.read_csv(file.file)

    # ✅ AGGREGATION (THIS IS WHAT YOU WANTED)
    agg_df = (
        df
        .groupby(["date", "city", "disease"], as_index=False)
        .agg({
            "admissions": "sum",
            "icu_occupancy": "sum"
        })
    )

    # Store ONLY aggregated rows
    for _, row in agg_df.iterrows():
        record = HospitalRecord(
            date=row["date"],
            region=row["city"],
            syndrome="AGGREGATED",
            disease=row["disease"],
            admissions=row["admissions"],
            icu_occupancy=row["icu_occupancy"]
        )
        db.add(record)

    db.commit()

    analysis = run_analysis(agg_df)

    return {
        "status": "success",
        "rows_inserted": len(agg_df),
        "analysis_preview": analysis
    }
