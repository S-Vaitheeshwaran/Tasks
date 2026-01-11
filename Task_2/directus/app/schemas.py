from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class ExperimentCreate(BaseModel):
    name: str
    experiment_type: Literal["llm"]
    status: Literal["created", "running", "completed", "failed"]

class ExperimentResponse(ExperimentCreate):
    id: int
    created_at: datetime
