from pydantic import BaseModel
from typing import List, Optional

class ForecastDay(BaseModel):
    date: str
    temp_max: float
    temp_min: float
    rain_prob: Optional[float] = None

class PlanRequest(BaseModel):
    query: str
    weather: Optional[bool] = None
    places: Optional[bool] = None
    place: Optional[str] = None

class WeatherData(BaseModel):
    current_temperature: float
    current_rain_chance: float
    summary: str
    forecast: List[ForecastDay]

class TourismQueryRequest(BaseModel):
    query: str
    place: Optional[str] = None

class TourismQueryResponse(BaseModel):
    place: str
    used_agents: List[str]
    weather_summary: Optional[str] = None
    places: Optional[List[str]] = None
    message: str
    error: Optional[str] = None

class PlanResponse(BaseModel):
    place: str
    used_agents: List[str]
    weather: Optional[WeatherData] = None
    places: Optional[List[str]] = None
    message: str
    error: Optional[str] = None
