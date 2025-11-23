import pytest
from backend.app.services.geocoding_service import GeocodingService

@pytest.mark.asyncio
async def test_geocoding_service(monkeypatch):
    async def mock_get(*args, **kwargs):
        class MockResponse:
            def json(self):
                return [{"lat": "12.97", "lon": "77.59"}]
        return MockResponse()
    service = GeocodingService()
    monkeypatch.setattr("httpx.AsyncClient.get", mock_get)
    coords = await service.get_coordinates("Bangalore")
    assert coords["lat"] == 12.97
    assert coords["lon"] == 77.59
