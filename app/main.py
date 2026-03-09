from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title = "AI Orchestrator")

app.include_router(router)