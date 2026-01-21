from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.models import User

app = FastAPI(title="PrevAI Backend")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()

    if not user or user.password != password:
        return {"status": "error", "message": "Invalid credentials"}

    return {
        "status": "success",
        "role": user.role,
        "email": user.email
    }
