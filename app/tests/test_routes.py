
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_list_events():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/events")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_stats():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/stats")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
