import httpx

class WeatherService:
    async def get_weather(self, coords: dict) -> dict:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": coords["lat"],
            "longitude": coords["lon"],
            "current_weather": True,
            "hourly": "precipitation_probability",
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
            "timezone": "auto"
        }
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, params=params)
            data = resp.json()
            if "current_weather" not in data:
                return None
            temp = data["current_weather"].get("temperature")
            rain_chance = None
            if "hourly" in data and "precipitation_probability" in data["hourly"]:
                rain_chance = data["hourly"]["precipitation_probability"][0]
            # Build forecast list
            forecast = []
            if "daily" in data:
                dates = data["daily"].get("time", [])
                maxs = data["daily"].get("temperature_2m_max", [])
                mins = data["daily"].get("temperature_2m_min", [])
                rain_probs = data["daily"].get("precipitation_probability_max", [])
                for i in range(min(len(dates), 7)):
                    forecast.append({
                        "date": dates[i],
                        "temp_max": maxs[i] if i < len(maxs) else None,
                        "temp_min": mins[i] if i < len(mins) else None,
                        "rain_prob": rain_probs[i] if i < len(rain_probs) else None
                    })
            return {
                "temperature": temp,
                "rain_chance": rain_chance or 0,
                "forecast": forecast
            }
