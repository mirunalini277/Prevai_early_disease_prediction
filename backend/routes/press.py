from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime

from backend.database import get_db
from backend.models import PressRelease

router = APIRouter(
    prefix="/press",
    tags=["Press"]
)

class PressRequest(BaseModel):
    title: str
    content: str

@router.post("/")
def publish_press(req: PressRequest, db: Session = Depends(get_db)):
    press = PressRelease(
        title=req.title,
        content=req.content
    )
    db.add(press)
    db.commit()
    return {"message": "Press published"}

@router.get("/")
def get_press(db: Session = Depends(get_db)):
    rows = db.query(PressRelease).order_by(
        PressRelease.created_at.desc()
    ).all()

    return [
        {
            "title": r.title,
            "content": r.content,
            "date": r.created_at.strftime("%Y-%m-%d %H:%M")
        }
        for r in rows
    ]
