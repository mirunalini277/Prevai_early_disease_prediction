from fastapi import FastAPI

from backend.routes import (
    auth_routes,
    hospital_routes,
    ministry_routes,
    press_routes
)

app = FastAPI(title="PrevAI Backend")

# Register all routers
app.include_router(auth_routes.router)
app.include_router(hospital_routes.router)
app.include_router(ministry_routes.router)
app.include_router(press_routes.router)

@app.get("/")
def root():
    return {"status": "Backend running"}
