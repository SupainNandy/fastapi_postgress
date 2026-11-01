"""Pydantic schemas package for request/response validation."""
from app.schemas.book import BookCreate, BookResponse
from app.schemas.book_issue import (
    BookIssueResponse,
    BorrowBooksRequest,
    ReturnBookResponse,
)
from app.schemas.student import StudentCreate, StudentResponse
from app.schemas.todo import TodoCreate, TodoResponse, TodoUpdate

__all__ = [
    "TodoCreate",
    "TodoUpdate",
    "TodoResponse",
    "StudentCreate",
    "StudentResponse",
    "BookCreate",
    "BookResponse",
    "BorrowBooksRequest",
    "BookIssueResponse",
    "ReturnBookResponse",
]
