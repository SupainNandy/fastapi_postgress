from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class BorrowBooksRequest(BaseModel):
    """Schema for a student borrowing one or multiple books at a time."""

    student_id: int = Field(..., description="ID of the borrowing student")
    book_ids: list[int] = Field(..., min_length=1, description="List of book IDs being borrowed")
    days_valid: int = Field(default=7, ge=1, le=90, description="Number of days until the book must be returned")


class BookIssueResponse(BaseModel):
    """Schema for a single book borrowing transaction record."""

    id: int
    student_id: int
    book_id: int
    issued_at: datetime
    due_date: datetime
    returned_at: datetime | None = None
    fine_amount: int
    status: str

    model_config = ConfigDict(from_attributes=True)


class ReturnBookResponse(BaseModel):
    """Schema returned after a book is returned, including fine details."""

    book_issue_id: int
    book_id: int
    student_id: int
    returned_at: datetime
    due_date: datetime
    days_overdue: int
    fine_amount: int
    message: str
