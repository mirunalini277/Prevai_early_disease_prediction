from fastapi import APIRouter

router = APIRouter(prefix="/ministry")

@router.post("/register-hospital")
def register_hospital():
    return {"status": "success", "message": "Hospital registered"}

@router.get("/dashboard")
def dashboard():
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
