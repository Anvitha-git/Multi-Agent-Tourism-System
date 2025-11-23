# Architecture – Multi-Agent Tourism System

## Overview
- Parent agent: TourismAgent (orchestrates query parsing and agent calls)
- Child agents: WeatherAgent (weather), PlacesAgent (tourist attractions)
- Services: Geocoding (Nominatim), Weather (Open-Meteo), Places (Overpass)
- Error handling: Custom exceptions, clear error codes

## Backend Modules
- `app/agents/`: Agent logic
- `app/services/`: API wrappers
- `app/routers/`: FastAPI routes
- `app/models/`: Pydantic schemas
- `app/utils/`: Logging, exceptions

## Frontend Modules
- `src/api/`: API client
- `src/components/`: UI components
- `src/types/`: TypeScript types

See README.md for more details.