from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llava_service import (
    answer_followup_question
)

router = APIRouter()


class QuestionRequest(BaseModel):
    context: str
    question: str


@router.post("/ask")
async def ask_question(
    request: QuestionRequest
):

    answer = answer_followup_question(
        request.context,
        request.question
    )

    return {
        "answer": answer
    }