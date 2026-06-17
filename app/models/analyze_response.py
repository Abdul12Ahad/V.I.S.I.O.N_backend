from pydantic import BaseModel


class AnalyzeResponse(BaseModel):

    analysis: str

    category: str

    width: int
    height: int

    size_kb: float

    image_path: str