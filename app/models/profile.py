from sqlalchemy import Column, String, Integer, JSON, DateTime, Text
from sqlalchemy.sql import func

from app.models.base import Base

class Profile(Base):
    __tablename__ = "profiles"
    
    # Primary key
    id = Column(String, primary_key=True, index=True)
    
    # LinkedIn URL
    profile_url = Column(String(500), unique=True, index=True, nullable=False)
    profile_hash = Column(String(64), unique=True, index=True)  # For caching
    
    # Basic info
    profile_name = Column(String(200), nullable=True)
    
    # Heatmap data (JSON format: {"2024-01-01": 3, "2024-01-02": 1})
    heatmap_data = Column(JSON, nullable=False, default=dict)
    
    # Metrics
    total_posts = Column(Integer, default=0)
    streak_days = Column(Integer, default=0)
    consistency_score = Column(Integer, default=0)  # 0-100
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<Profile(id={self.id}, url={self.profile_url[:30]}...)>"