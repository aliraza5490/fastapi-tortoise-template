import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from webbrowser import get

from fastapi import FastAPI
from tortoise import Tortoise, generate_config
from tortoise.contrib.fastapi import RegisterTortoise, tortoise_exception_handlers

import os
from functools import partial

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
    print("environment",getattr(app.state, "testing", None))
    # app startup
    async with register_orm(app):
        # db connected
        yield
        # app teardown
    # db connections closed
    
