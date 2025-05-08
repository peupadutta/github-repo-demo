
from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncio
from app.api.routes import api_router
from app.services.fetcher import fetch_and_store
from tasks import start_fetcher

@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    task = asyncio.create_task(start_fetcher())
    await fetch_and_store()
    yield
    # SHUTDOWN
    # Clean up resources if needed

app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
