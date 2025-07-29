from fastapi import APIRouter

from src.routes.home_routes import router

api_router = APIRouter(prefix='/api/v1')

api_router.include_router(
    router
)