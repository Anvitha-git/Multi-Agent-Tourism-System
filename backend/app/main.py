from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import tourism
from .utils.logging import setup_logging

setup_logging()

app = FastAPI(title="Multi-Agent Tourism System")

# CORS configuration for Render backend consumed by Vercel frontend
allowed_origins = [
	"http://localhost:5173",  # local dev
	"https://multi-agent-tourism-system.vercel.app",  # replace with actual Vercel domain
]
app.add_middleware(
	CORSMiddleware,
	allow_origins=allowed_origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.get("/")
async def root():
	return {"message": "Multi-Agent Tourism System API", "status": "running"}

@app.get("/health")
async def health_check():
	return {"status": "healthy"}

app.include_router(tourism.router, prefix="/api/v1/tourism", tags=["Tourism"])
