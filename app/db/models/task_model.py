from sqlalchemy import Column, Integer, String, DateTime, Text
from app.db.base import Base
from datetime import datetime

class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, default=None)
    title = Column(String(255))
    description = Column(Text)
    state = Column(Integer, nullable=False, default=0)
    update_at = Column(DateTime, default=None, nullable=True)
    created_at = Column(
        DateTime, default=lambda: datetime.now(), nullable=True)
