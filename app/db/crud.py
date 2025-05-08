
from sqlalchemy import select, func, delete
from app.db.models import Event
from app.db.session import SessionLocal

async def insert_event(event_data):
    async with SessionLocal() as session:
        exists = await session.get(Event, event_data["event_id"])
        if not exists:
            event = Event(**event_data)
            session.add(event)
            await session.commit()

async def get_events(skip=0, limit=100):
    async with SessionLocal() as session:
        result = await session.execute(select(Event).offset(skip).limit(limit))
        return result.scalars().all()

async def get_events_by_user(user_id: str):
    async with SessionLocal() as session:
        result = await session.execute(select(Event).where(Event.user_id == user_id))
        return result.scalars().all()

async def get_stats():
    async with SessionLocal() as session:
        result = await session.execute(select(Event.type, func.count()).group_by(Event.type))
        return result.all()

async def delete_all_events():
    async with SessionLocal() as session:
        await session.execute(delete(Event))
        await session.commit()
