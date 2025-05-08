
import asyncio
from app.services.fetcher import fetch_and_store

async def start_fetcher():
    while True:
        await fetch_and_store()
        await asyncio.sleep(60)
