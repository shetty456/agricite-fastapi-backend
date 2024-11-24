import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_todo():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/todos/", json={"title": "Test Todo", "description": "Test Description"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Todo"
