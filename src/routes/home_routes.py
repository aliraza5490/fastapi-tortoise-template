from fastapi import APIRouter, Depends
from typing import Union

from src.settings import settings
from src.utillities.auth import get_user_from_token

router = APIRouter(prefix="/home", tags=["home"])

@router.get("/")
def read_root(user = Depends(get_user_from_token)):
    return {"Hello": settings.FRONTEND_HOST, "user": user}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None, user = Depends(get_user_from_token)):
    return {"item_id": item_id, "q": q, "user": user}