# Job business logic
from sqlalchemy.orm import Session
from app.models.job import Job, JobStatus
from app.schemas.job import JobCreate


class JobService:
    @staticmethod
    def create_job(db: Session, job: JobCreate) -> Job:
        """Create a new scraping job"""
        db_job = Job(**job.model_dump())
        db.add(db_job)
        db.commit()
        db.refresh(db_job)
        return db_job
    
    @staticmethod
    def get_job(db: Session, job_id: int) -> Job | None:
        """Get job by ID"""
        return db.query(Job).filter(Job.id == job_id).first()
    
    @staticmethod
    def update_job_status(db: Session, job_id: int, status: JobStatus, error_message: str | None = None) -> Job | None:
        """Update job status"""
        job = db.query(Job).filter(Job.id == job_id).first()
        if job:
            job.status = status
            if error_message:
                job.error_message = error_message
            db.commit()
            db.refresh(job)
        return job
