from fastapi import APIRouter

from app.database import (
    get_history
)

router = APIRouter()


@router.get("/history")
def history():

    return get_history()