from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from backend.database import SessionLocal
from backend.models import User

router = APIRouter(prefix="/ministry", tags=["Ministry"])

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Request schema
class HospitalCreate(BaseModel):
    email: str
    password: str
    region: str

@router.post("/register-hospital")
def register_hospital(data: HospitalCreate, db: Session = Depends(get_db)):
    # Check if already exists
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        return {
            "status": "error",
            "message": "Hospital already exists"
        }

    hospital = User(
        email=data.email,
        password=data.password,
        role="hospital",
        region=data.region
    )

    db.add(hospital)
    db.commit()

    return {
        "status": "success",
        "message": "Hospital registered successfully"
    }

@router.get("/dashboard")
def dashboard():
    # Dummy data for now
    return [
        {
            "region": "Chennai",
            "disease": "Dengue",
            "category": "CONFIRMED",
            "actual": 120,
            "expected": 80,
            "risk": "High"
        }
    ]
