from fastapi import FastAPI
from app.experiments.router import router as experiment_router

app = FastAPI(title="LLM Experiment Service")

app.include_router(experiment_router)
