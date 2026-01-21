from fastapi import APIRouter

router = APIRouter()

@router.post("/press-release")
def publish_press():
    return {"status": "success"}

@router.get("/press-releases")
def get_press():
    return []
