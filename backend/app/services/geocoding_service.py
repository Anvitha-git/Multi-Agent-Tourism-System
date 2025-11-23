import httpx
from ..config import USER_AGENT

class GeocodingService:
    async def get_coordinates(self, place: str) -> dict:
        url = "https://nominatim.openstreetmap.org/search"
        params = {"q": place, "format": "json", "limit": 1}
        headers = {"User-Agent": USER_AGENT}
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, params=params, headers=headers)
            data = resp.json()
            if not data:
                return None
            lat = data[0].get("lat")
            lon = data[0].get("lon")
            if lat and lon:
                return {"lat": float(lat), "lon": float(lon)}
            return None
