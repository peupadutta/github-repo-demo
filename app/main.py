
import asyncio
from fastapi import FastAPI
from app.api.routes import router
from app.tasks import start_fetcher
from app.db.models import Base
from app.db.session import engine

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    asyncio.create_task(start_fetcher())
