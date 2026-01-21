from fastapi import FastAPI
from routes import auth_routes, hospital_routes, ministry_routes, press_routes

app = FastAPI(title="PrevAI Backend")

app.include_router(auth_routes.router)
app.include_router(hospital_routes.router)
app.include_router(ministry_routes.router)
app.include_router(press_routes.router)

@app.get("/health")
def health_check():
    return {"status": "Backend is running"}
