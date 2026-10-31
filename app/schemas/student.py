from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class StudentBase(BaseModel):
    """Base schema containing common student attributes."""

    name: str = Field(..., min_length=2, max_length=100, description="Full name of the student")
    address: str = Field(..., min_length=3, max_length=255, description="Residential address")
    age: int | None = Field(default=None, ge=1, le=120, description="Optional age in years")


class StudentCreate(StudentBase):
    """Schema for creating a new student."""

    pass


class StudentResponse(StudentBase):
    """Schema for returning student details to clients."""

    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
