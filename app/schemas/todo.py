from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class TodoBase(BaseModel):
    """Base schema for shared Todo attributes."""

    content: str = Field(..., min_length=1, max_length=500, description="The content of the todo item")
    is_completed: bool = Field(default=False, description="Completion status")


class TodoCreate(TodoBase):
    """Schema for creating a new Todo item."""

    pass


class TodoUpdate(BaseModel):
    """Schema for updating an existing Todo item."""

    content: str | None = Field(default=None, min_length=1, max_length=500)
    is_completed: bool | None = Field(default=None)


class TodoResponse(TodoBase):
    """Schema for returning a Todo item to the client."""

    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
