# API Reference – Multi-Agent Tourism System

## POST /api/v1/tourism/query

Request:
```
{
  "query": "I’m going to go to Bangalore, what is the temperature there? And what are the places I can visit?"
}
```

Response:
```
{
  "place": "Bangalore",
  "used_agents": ["WeatherAgent", "PlacesAgent"],
  "weather_summary": "In Bangalore it’s currently 24°C with a chance of 35% to rain.",
  "places": ["Lalbagh", "Bangalore Palace", ...],
  "message": "In Bangalore it’s currently 24°C with a chance of 35% to rain. And these are the places you can go: - Lalbagh - Bangalore Palace ...",
  "error": null
}
```

Error example:
```
{
  "place": "asldkfjalskdf",
  "used_agents": [],
  "weather_summary": null,
  "places": null,
  "message": "I’m not sure this place exists or I can’t find it in my data.",
  "error": "PLACE_NOT_FOUND"
}
```
