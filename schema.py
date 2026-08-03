from typing import List, Literal
from pydantic import BaseModel, Field


class ChatResponse(BaseModel):
    answer: str = Field(
        description="Complete answer to the user's question."
    )

    summary: str = Field(
        description="A short summary of the answer."
    )

    confidence: float = Field(
        ge=0,
        le=1,
        description="Confidence score between 0 and 1."
    )

    category: Literal[
        "Programming",
        "Mathematics",
        "General"
    ] = Field(
        description="Detected category of the user's question."
    )

    keywords: List[str] = Field(
        description="Important keywords extracted from the response."
    )