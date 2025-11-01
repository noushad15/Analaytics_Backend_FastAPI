from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session

router = APIRouter(tags=["analytics"])

@router.get("/health", summary="Service health check")
async def health(session: AsyncSession = Depends(get_session)):
    try:
        await session.execute("SELECT 1")
        db_status = "ok"
    except Exception as e:
        db_status = f"error: {e.__class__.__name__}"
    return {"service": "ok", "database": db_status}

@router.get("/sample-metric", summary="Sample analytics metric")
async def sample_metric():
    return {"metric_name": "sessions", "metric_value": 1234}
