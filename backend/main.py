from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import (
    auth_routes,
    hospital_routes,
    ministry_routes,
    press_routes
)

app = FastAPI(title="PrevAI Backend")

# ---------- CORS (REQUIRED FOR FRONTEND) ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Routers ----------
app.include_router(auth_routes.router)
app.include_router(hospital_routes.router)
app.include_router(ministry_routes.router)
app.include_router(press_routes.router)

# ---------- Health Check ----------
@app.get("/")
def root():
    return {"status": "Backend running"}
