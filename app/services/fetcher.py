
import httpx
from app.db.crud import insert_event
from datetime import datetime

async def fetch_and_store():
    async with httpx.AsyncClient() as client:
        res = await client.get("https://api.github.com/events")
        events = res.json()
        for e in events:
            event_data = {
                "event_id": e["id"],
                "type": e["type"],
                "user_id": e["actor"]["login"],
                "repo": e["repo"]["name"],
                "timestamp": datetime.strptime(e["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            }
            await insert_event(event_data)
