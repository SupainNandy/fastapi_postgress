from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentResponse

router = APIRouter()

DbSession = Annotated[Session, Depends(get_db)]


@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(payload: StudentCreate, db: DbSession):
    """Create a new Student record in PostgreSQL."""
    db_student = Student(
        name=payload.name,
        address=payload.address,
        age=payload.age,
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@router.get("/", response_model=list[StudentResponse])
def list_students(
    db: DbSession,
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
):
    """Retrieve all students (paginated)."""
    stmt = select(Student).offset(skip).limit(limit)
    return db.scalars(stmt).all()


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: DbSession):
    """Retrieve a student by their ID."""
    db_student = db.get(Student, student_id)
    if not db_student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {student_id} not found",
        )
    return db_student
