from fastapi import APIRouter
from typing import Union

from src.settings import settings

router = APIRouter(prefix="/home", tags=["home"])

@router.get("/")
def read_root():
    return {"Hello": settings.FRONTEND_HOST}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}