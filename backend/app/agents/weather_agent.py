from .base import BaseAgent
from ..services.weather_service import WeatherService

class WeatherAgent(BaseAgent):
    def __init__(self):
        self.weather_service = WeatherService()

    async def run(self, coords: dict, place: str) -> dict:
        weather = await self.weather_service.get_weather(coords)
        if not weather:
            return None
        temp = weather.get("temperature")
        rain = weather.get("rain_chance")
        forecast = weather.get("forecast", [])
        summary = f"In {place} it’s currently {temp}°C with a chance of {rain}% to rain."
        return {
            "current_temperature": temp,
            "current_rain_chance": rain,
            "summary": summary,
            "forecast": forecast
        }
