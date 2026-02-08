# Background job runner
import asyncio
from app.core.database import SessionLocal
from app.models.job import JobStatus
from app.services.job_service import JobService


class JobRunner:
    """Background worker to process scraping jobs"""
    
    def __init__(self):
        self.running = False
    
    async def start(self):
        """Start the job runner"""
        self.running = True
        while self.running:
            await self.process_pending_jobs()
            await asyncio.sleep(10)  # Check for new jobs every 10 seconds
    
    async def process_pending_jobs(self):
        """Process all pending jobs"""
        db = SessionLocal()
        try:
            # TODO: Fetch pending jobs and process them
            pass
        finally:
            db.close()
    
    def stop(self):
        """Stop the job runner"""
        self.running = False
