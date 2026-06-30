from fastapi import APIRouter
from app.schemas.metrics import MetricsIn
from app.services.metrics_service import process_metrics

router = APIRouter()

@router.post("/metrics")
def ingest_metrics(data: MetricsIn):
    return process_metrics(data)
