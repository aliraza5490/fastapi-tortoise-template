from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.lifespan import lifespan
from src.routes import api_router
from src.settings import settings
from tortoise.contrib.fastapi import tortoise_exception_handlers

app = FastAPI(title="FastAPI Template", description="API documentation", version="1.0.0", lifespan=lifespan, exception_handlers=tortoise_exception_handlers())

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.all_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(api_router)