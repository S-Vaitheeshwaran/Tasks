from fastapi import FastAPI
from app.routes.experiments import router as experiment_router

app = FastAPI(title="Experiment Metadata Service")

app.include_router(experiment_router)

@app.get("/")
def health():
    return {"status": "Backend running successfully"}
