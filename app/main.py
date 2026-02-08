from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.database import engine
from app.models import Base
from app.api.health import router as health_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Starting LinkedIn Heatmap Backend...")
    
    # Create database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Database tables created")
    
    yield
    
    # Shutdown
    await engine.dispose()
    print("👋 Application shutting down...")

# Create FastAPI app
app = FastAPI(
    title="LinkedIn Heatmap API",
    description="API to analyze LinkedIn public activity and generate heatmaps",
    version="0.1.0",
    lifespan=lifespan,
)

# Include routers
app.include_router(health_router)

@app.get("/")
async def root():
    return {
        "message": "LinkedIn Heatmap API",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health"
    }