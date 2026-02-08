from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from datetime import datetime

from app.core.database import get_db

router = APIRouter(tags=["health"])

@router.get("/health")
async def health_check(db: AsyncSession = Depends(get_db)):
    """Simple health check endpoint"""
    # Test database connection
    try:
        await db.execute(text("SELECT 1"))
        db_status = "healthy"
    except Exception as e:
        print("DB health error:", e)
        db_status = "unhealthy"
    
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(),
        "database": db_status,
        "service": "linkedin-heatmap-api"
    }