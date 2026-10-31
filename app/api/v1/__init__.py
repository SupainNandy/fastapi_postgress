from fastapi import APIRouter

from app.api.v1.endpoints import students, todos

api_router = APIRouter()
api_router.include_router(todos.router, prefix="/todos", tags=["Todos"])
api_router.include_router(students.router, prefix="/students", tags=["Students"])
