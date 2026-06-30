from pydantic import BaseModel
from datetime import datetime


class MetricsIn(BaseModel):
    server_id: str
    cpu: float
    ram: float
    disk: float
    network: float
    timestamp: datetime
