from fastapi import APIRouter

router = APIRouter(prefix="/hospital")

@router.post("/upload-csv")
def upload_csv():
    return {"status": "success", "message": "CSV received"}
