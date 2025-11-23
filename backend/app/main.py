from fastapi import FastAPI
from .routers import tourism
from .utils.logging import setup_logging

setup_logging()

app = FastAPI(title="Multi-Agent Tourism System")

app.include_router(tourism.router, prefix="/api/v1/tourism", tags=["Tourism"])
