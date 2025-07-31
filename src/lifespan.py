from functools import partial
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from fastapi import FastAPI, logger
from tortoise.contrib.fastapi import RegisterTortoise, tortoise_exception_handlers
from tortoise.contrib.fastapi import RegisterTortoise

from src.settings import settings

MODELS = [
    'aerich.models',
    'src.models.user'
]

TORTOISE_ORM = {
    "connections": {"default": str(settings.SQLALCHEMY_DATABASE_URI)},
    "apps": {
        "models": {
            "models": MODELS,
            "default_connection": "default",
        },
    },
}

register_orm = partial(
    RegisterTortoise,
    config=TORTOISE_ORM,
    generate_schemas=True,
)

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # app startup
    async with register_orm(app):
        # db connected
        logger.logger.info("Database connected")
        yield
        # app teardown
    # db connections closed
    
