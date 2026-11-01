from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.book import Book
from app.models.book_issue import BookIssue
from app.models.student import Student
from app.schemas.book_issue import (
    BookIssueResponse,
    BorrowBooksRequest,
    ReturnBookResponse,
)

router = APIRouter()

DbSession = Annotated[Session, Depends(get_db)]

DAILY_FINE_RATE = 50  # ₹50 per day for late returns


@router.post("/borrow", response_model=list[BookIssueResponse], status_code=status.HTTP_201_CREATED)
def borrow_books(payload: BorrowBooksRequest, db: DbSession):
    """Borrow one or multiple books at a time for a student."""
    # 1. Verify student exists
    student = db.get(Student, payload.student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {payload.student_id} not found",
        )

    now = datetime.now(timezone.utc)
    due_date = now + timedelta(days=payload.days_valid)

    issued_records: list[BookIssue] = []

    # 2. Check each requested book
    for book_id in payload.book_ids:
        book = db.get(Book, book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with id {book_id} not found in library",
            )
        if book.available_copies <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Book '{book.title}' (ID {book_id}) has no available copies left",
            )

        # Decrement available inventory
        book.available_copies -= 1

        # Create borrow transaction
        issue = BookIssue(
            student_id=student.id,
            book_id=book.id,
            issued_at=now,
            due_date=due_date,
            status="BORROWED",
            fine_amount=0,
        )
        db.add(issue)
        issued_records.append(issue)

    # Commit all changes atomically
    db.commit()
    for record in issued_records:
        db.refresh(record)

    return issued_records


@router.post("/return/{issue_id}", response_model=ReturnBookResponse)
def return_book(issue_id: int, db: DbSession):
    """Return a borrowed book, update inventory, and calculate any late fine (₹50/day)."""
    issue = db.get(BookIssue, issue_id)
    if not issue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Borrow record with id {issue_id} not found",
        )

    if issue.status == "RETURNED":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This book has already been returned.",
        )

    now = datetime.now(timezone.utc)
    issue.returned_at = now
    issue.status = "RETURNED"

    # Restore inventory
    book = db.get(Book, issue.book_id)
    if book:
        book.available_copies += 1

    # Calculate fine (₹50 per day past due date)
    days_overdue = 0
    fine_amount = 0

    if now > issue.due_date:
        days_overdue = (now.date() - issue.due_date.date()).days
        if days_overdue > 0:
            fine_amount = days_overdue * DAILY_FINE_RATE

    issue.fine_amount = fine_amount
    db.commit()

    message = (
        f"Book returned successfully. Late fine applied: ₹{fine_amount} ({days_overdue} days overdue)."
        if fine_amount > 0
        else "Book returned on time! No fine applicable."
    )

    return ReturnBookResponse(
        book_issue_id=issue.id,
        book_id=issue.book_id,
        student_id=issue.student_id,
        returned_at=issue.returned_at,
        due_date=issue.due_date,
        days_overdue=days_overdue,
        fine_amount=fine_amount,
        message=message,
    )


@router.get("/issues", response_model=list[BookIssueResponse])
def list_borrow_records(
    db: DbSession,
    student_id: int | None = None,
    status_filter: str | None = None,
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
):
    """List borrowing history and active book loans."""
    stmt = select(BookIssue).offset(skip).limit(limit)
    if student_id is not None:
        stmt = stmt.where(BookIssue.student_id == student_id)
    if status_filter:
        stmt = stmt.where(BookIssue.status == status_filter.upper())

    return db.scalars(stmt).all()
