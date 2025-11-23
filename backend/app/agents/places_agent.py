from .base import BaseAgent
from ..services.places_service import PlacesService

class PlacesAgent(BaseAgent):
    def __init__(self):
        self.places_service = PlacesService()

    async def run(self, coords: dict, place: str) -> list:
        places = await self.places_service.get_places(coords)
        return places or []
