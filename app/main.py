from fastapi import FastAPI
from app.config import settings

app = FastAPI(title=settings.app_name)

@app.get("/")
def read_root():
    return {
        "message": "MarketMind Intelligence API",
        "status": "running",
        "version": "0.1.0",
    }

app.get("/health")
def health_check():
    return {"status": "healthy"}