import pytest
from backend.app.agents.places_agent import PlacesAgent

@pytest.mark.asyncio
async def test_places_agent_run(monkeypatch):
    async def mock_get_places(coords):
        return ["Lalbagh", "Bangalore Palace"]
    agent = PlacesAgent()
    agent.places_service.get_places = mock_get_places
    result = await agent.run({"lat": 12.97, "lon": 77.59}, "Bangalore")
    assert "Lalbagh" in result
    assert "Bangalore Palace" in result
