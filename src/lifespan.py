import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise import Tortoise, generate_config
from tortoise.contrib.fastapi import RegisterTortoise, tortoise_exception_handlers

import os
from functools import partial

from tortoise.contrib.fastapi import RegisterTortoise

from src.settings import settings


MODELS = [
    # 'aerich.models',
    'src.models.user'
]


register_orm = partial(
    RegisterTortoise,
    db_url=str(settings.SQLALCHEMY_DATABASE_URI),
    modules={"models": MODELS},
    generate_schemas=True,
)


@asynccontextmanager
async def lifespan_test(app: FastAPI) -> AsyncGenerator[None, None]:
    config = generate_config(
        str(settings.SQLALCHEMY_DATABASE_URI),
        app_modules={"models": MODELS},
        testing=True,
        connection_label="models",
    )
    async with RegisterTortoise(
        app=app,
        config=config,
        generate_schemas=True,
        _create_db=True,
    ):
        # db connected
        yield
        # app teardown
    # db connections closed
    await Tortoise._drop_databases()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    if getattr(app.state, "testing", None):
        async with lifespan_test(app) as _:
            yield
    else:
        # app startup
        async with register_orm(app):
            # db connected
            yield
            # app teardown
        # db connections closed

    

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Setup: Initialize before app starts
#     yield  # This is crucial - it yields control back to FastAPI
#     # Cleanup: Code after this will run when app shuts down
#     # You can add cleanup code here if needed
#     pass
