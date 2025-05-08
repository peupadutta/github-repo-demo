
from fastapi import APIRouter
from app.db.crud import get_events, get_events_by_user, get_stats, delete_all_events

router = APIRouter()

@router.get("/events")
async def list_events(skip: int = 0, limit: int = 100):
    return await get_events(skip, limit)

@router.get("/events/{user_id}")
async def list_events_for_user(user_id: str):
    return await get_events_by_user(user_id)

@router.get("/stats")
async def stats():
    return await get_stats()

@router.delete("/events")
async def delete_events():
    await delete_all_events()
    return {"status": "deleted"}
