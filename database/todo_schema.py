from sqlalchemy import Column, Integer, String, Boolean, Datetime

from ..database.Schema.db import base

from datetime import datetime,timezone

class Todo(base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    isCompleted = Column(Boolean, default=False, nullable=False)
    created_at = Column(Datetime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(Datetime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)