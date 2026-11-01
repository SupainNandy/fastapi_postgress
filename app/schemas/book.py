from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class BookBase(BaseModel):
    """Base schema for shared book attributes."""

    title: str = Field(..., min_length=1, max_length=200, description="Title of the book")
    author: str = Field(..., min_length=1, max_length=100, description="Author of the book")
    isbn: str | None = Field(default=None, max_length=20, description="International Standard Book Number")
    total_copies: int = Field(default=1, ge=1, description="Total inventory count")


class BookCreate(BookBase):
    """Schema for adding a new book to the library."""

    pass


class BookResponse(BookBase):
    """Schema for returning book information."""

    id: int
    available_copies: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
