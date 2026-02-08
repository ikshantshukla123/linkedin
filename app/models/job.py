# Job database model
from sqlalchemy import String, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
import enum

from app.models.base import Base


class JobStatus(str, enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class Job(Base):
    __tablename__ = "jobs"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    profile_id: Mapped[int] = mapped_column()
    job_type: Mapped[str] = mapped_column(String)  # scrape_profile, scrape_activities
    status: Mapped[JobStatus] = mapped_column(Enum(JobStatus), default=JobStatus.PENDING)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    error_message: Mapped[str | None] = mapped_column(String, nullable=True)
