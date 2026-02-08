# Activity database model
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.models.base import Base


class Activity(Base):
    __tablename__ = "activities"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    profile_id: Mapped[int] = mapped_column(ForeignKey("profiles.id"))
    activity_type: Mapped[str] = mapped_column(String)  # post, comment, reaction, etc.
    activity_date: Mapped[datetime] = mapped_column(DateTime)
    content: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    # Relationship
    # profile = relationship("Profile", back_populates="activities")
