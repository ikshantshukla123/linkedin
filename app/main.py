from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(title="LinkedIn Heatmap Backend")

app.include_router(health_router)

@app.get("/")
async def root():
    return {"status": "ok"}
@app.get("/favicon.ico")
async def favicon():
    return Response(status_code=204)
