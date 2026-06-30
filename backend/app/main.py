from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.metrics import router as metrics_router

app = FastAPI(title="AI Cloud Platform")

app.include_router(health_router)
app.include_router(metrics_router)


@app.get("/")
def root():
    return {"message": "AI Cloud Platform running"}
