# Job request/response schemas
from pydantic import BaseModel
from datetime import datetime


class JobBase(BaseModel):
    profile_id: int
    job_type: str


class JobCreate(JobBase):
    pass


class JobResponse(JobBase):
    id: int
    status: str
    created_at: datetime
    completed_at: datetime | None = None
    error_message: str | None = None
    
    class Config:
        from_attributes = True
