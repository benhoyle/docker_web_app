"""File to define data models needed by the API."""

from pydantic import BaseModel


class TextData(BaseModel):
    """Data model for text data."""
    text: str

    class Config:
        """Config for data model."""
        schema_extra = {
            "example": {
                "text": "This is a test text."
            }
        }
