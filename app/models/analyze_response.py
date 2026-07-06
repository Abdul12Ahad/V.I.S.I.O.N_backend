from pydantic import BaseModel

class RelatedTopic(BaseModel):
    title: str
    points: list[str]

class AnalyzeResponse(BaseModel):

    description: str
    what_it_is: str
    how_it_works: str
    why_important: str
    fun_fact: str

    key_concepts: list[str]
    related_topics: list[RelatedTopic]
    learn_more: list[str]

    category: str

    width: int
    height: int

    size_kb: float

    image_path: str