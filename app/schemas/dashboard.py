from pydantic import BaseModel
from typing import Dict

class DashboardSummary(BaseModel):
    total_applications: int
    status_counts: Dict[str, int]
