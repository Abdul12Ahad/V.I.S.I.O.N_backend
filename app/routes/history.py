from fastapi import APIRouter

from app.database import (
    get_history,
    search_history
)

router = APIRouter()


@router.get("/history")
def history():

    return get_history()


@router.get("/history/search/{query}")
def history_search(query: str):

    return search_history(query)