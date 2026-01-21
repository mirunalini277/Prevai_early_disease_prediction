from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from backend.database import SessionLocal
from backend.models import User

router = APIRouter(tags=["Auth"])

# ---------- DB Dependency ----------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------- Request Schema ----------
class LoginRequest(BaseModel):
    email: str
    password: str

# ---------- Login ----------
@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()

    if not user or user.password != request.password:
        return {"status": "error", "message": "Invalid credentials"}

    return {
        "status": "success",
        "role": user.role,
        "email": user.email
    }
