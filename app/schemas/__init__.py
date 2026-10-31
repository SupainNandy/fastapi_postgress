"""Pydantic schemas package for request/response validation."""
from app.schemas.student import StudentCreate, StudentResponse
from app.schemas.todo import TodoCreate, TodoResponse, TodoUpdate

__all__ = [
    "TodoCreate",
    "TodoUpdate",
    "TodoResponse",
    "StudentCreate",
    "StudentResponse",
]
