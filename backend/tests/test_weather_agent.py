import pytest
from backend.app.agents.weather_agent import WeatherAgent

@pytest.mark.asyncio
async def test_weather_agent_run(monkeypatch):
    async def mock_get_weather(coords):
        return {"temperature": 25, "rain_chance": 40}
    agent = WeatherAgent()
    agent.weather_service.get_weather = mock_get_weather
    result = await agent.run({"lat": 12.97, "lon": 77.59}, "Bangalore")
    assert "25°C" in result
    assert "40%" in result
