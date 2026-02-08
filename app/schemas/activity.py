# Activity request/response schemas
from pydantic import BaseModel
from datetime import datetime


class ActivityBase(BaseModel):
    profile_id: int
    activity_type: str
    activity_date: datetime
    content: str | None = None


class ActivityCreate(ActivityBase):
    pass


class ActivityResponse(ActivityBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
