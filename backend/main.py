from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import os
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import PressRelease

app = FastAPI(title="PrevAI Backend", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
DATA_DIR = "data"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

# ---------------- LOGIN ----------------
from backend.models import User
from sqlalchemy.orm import Session
from fastapi import Depends

class LoginRequest(BaseModel):
    email: str
    password: str


@app.post("/login")
def login(req: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == req.email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if user.password != req.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "status": "success",
        "role": user.role,
        "email": user.email,
        "region": user.region
    }


@app.get("/")
def root():
    return {"status": "PrevAI backend running"}

# ---------------- PRESS RELEASE ----------------
class PressRequest(BaseModel):
    title: str
    content: str

@app.post("/press")
def publish_press(req: PressRequest, db: Session = Depends(get_db)):
    press = PressRelease(title=req.title, content=req.content)
    db.add(press)
    db.commit()
    return {"message": "Press released successfully"}

@app.get("/press")
def get_press(db: Session = Depends(get_db)):
    rows = (
        db.query(PressRelease)
        .order_by(PressRelease.created_at.desc())
        .all()
    )

    return [
        {
            "title": r.title,
            "content": r.content,
            "date": r.created_at.strftime("%Y-%m-%d %H:%M")
        }
        for r in rows
    ]

from backend.models import User
from sqlalchemy.orm import Session
from fastapi import Depends

class RegisterHospitalRequest(BaseModel):
    email: str
    password: str
    region: str

@app.post("/ministry/register-hospital")
def register_hospital(
    req: RegisterHospitalRequest,
    db: Session = Depends(get_db)
):
    existing = db.query(User).filter(User.email == req.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Hospital already exists")

    hospital = User(
        email=req.email,
        password=req.password,
        role="hospital",
        region=req.region
    )

    db.add(hospital)
    db.commit()

    return {"message": "Hospital registered successfully"}
@app.get("/demo/surveillance")
def demo_surveillance():
    return [
        {
            "date": "2026-01-10",
            "city": "Chennai",
            "disease": "Dengue",
            "reported": 120,
            "predicted": 85,
            "risk": "High"
        },
        {
            "date": "2026-01-10",
            "city": "Chennai",
            "disease": "Malaria",
            "reported": 40,
            "predicted": 45,
            "risk": "Normal"
        },
        {
            "date": "2026-01-10",
            "city": "Coimbatore",
            "disease": "Influenza",
            "reported": 70,
            "predicted": 60,
            "risk": "Medium"
        }
    ]

