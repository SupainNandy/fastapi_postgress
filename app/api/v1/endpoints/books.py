from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.book import Book
from app.schemas.book import BookCreate, BookResponse

router = APIRouter()

DbSession = Annotated[Session, Depends(get_db)]


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(payload: BookCreate, db: DbSession):
    """Add a new book to the library inventory."""
    db_book = Book(
        title=payload.title,
        author=payload.author,
        isbn=payload.isbn,
        total_copies=payload.total_copies,
        available_copies=payload.total_copies,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@router.get("/", response_model=list[BookResponse])
def list_books(
    db: DbSession,
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
):
    """Retrieve all library books (paginated)."""
    stmt = select(Book).offset(skip).limit(limit)
    return db.scalars(stmt).all()


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: DbSession):
    """Retrieve details of a specific book by ID."""
    db_book = db.get(Book, book_id)
    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found",
        )
    return db_book
