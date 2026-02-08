from pydantic import BaseModel, HttpUrl, Field
from typing import Dict, Optional
from datetime import datetime

class ProfileBase(BaseModel):
    profile_url: HttpUrl

class ProfileCreate(ProfileBase):
    pass

class ProfileResponse(ProfileBase):
    id: str
    profile_name: Optional[str] = None
    heatmap_data: Dict[str, int] = Field(default_factory=dict)
    total_posts: int = 0
    streak_days: int = 0
    consistency_score: int = 0
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True  # For SQLAlchemy model conversion

class HeatmapRequest(BaseModel):
    profile_url: HttpUrl
    force_refresh: bool = False

class HeatmapResponse(BaseModel):
    profile_id: str
    heatmap_data: Dict[str, int]
    is_cached: bool = True
    processing_time: float = 0.0