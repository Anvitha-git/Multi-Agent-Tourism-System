import pytest
from httpx import AsyncClient
from backend.app.main import app

@pytest.mark.asyncio
async def test_tourism_api_weather_only():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.post("/api/v1/tourism/query", json={"query": "I’m going to go to Bangalore, what is the temperature there?"})
        data = resp.json()
        assert "WeatherAgent" in data["used_agents"]
        assert data["weather_summary"]
        assert not data["places"]

@pytest.mark.asyncio
async def test_tourism_api_places_only():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.post("/api/v1/tourism/query", json={"query": "I’m going to go to Bangalore, let’s plan my trip."})
        data = resp.json()
        assert "PlacesAgent" in data["used_agents"]
        assert data["places"]
        assert not data["weather_summary"]

@pytest.mark.asyncio
async def test_tourism_api_both_agents():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.post("/api/v1/tourism/query", json={"query": "I’m going to go to Bangalore, what is the temperature there? And what are the places I can visit?"})
        data = resp.json()
        assert "WeatherAgent" in data["used_agents"]
        assert "PlacesAgent" in data["used_agents"]
        assert data["weather_summary"]
        assert data["places"]

@pytest.mark.asyncio
async def test_geocoding_invalid_place():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.post("/api/v1/tourism/query", json={"query": "I’m going to go to asldkfjalskdf, what is the temperature there?"})
        data = resp.json()
        assert data["error"] == "PLACE_NOT_FOUND"
        assert "not sure this place exists" in data["message"]
