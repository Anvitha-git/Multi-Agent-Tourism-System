from fastapi import APIRouter, HTTPException
from ..models.schemas import TourismQueryRequest, TourismQueryResponse, PlanRequest, PlanResponse, WeatherData, ForecastDay
from ..agents.tourism_agent import TourismAgent
from ..utils.exceptions import PlaceNotFoundException

router = APIRouter()
agent = TourismAgent()

@router.post("/query", response_model=TourismQueryResponse)
async def query_tourism(request: TourismQueryRequest):
    try:
        response = await agent.run(request)
        return response
    except PlaceNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        return TourismQueryResponse(
            place=request.place or "",
            used_agents=[],
            weather_summary=None,
            places=None,
            message="An unexpected error occurred. Please try again later.",
            error="SERVER_ERROR"
        )
@router.post("/plan", response_model=PlanResponse)
async def plan_trip(request: PlanRequest):
    try:
        response = await agent.plan(request)
        return response
    except PlaceNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        return PlanResponse(
            place=request.place or "",
            used_agents=[],
            weather=None,
            places=None,
            message="An unexpected error occurred. Please try again later.",
            error="SERVER_ERROR"
        )
