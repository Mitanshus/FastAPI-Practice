"""Import necessary modules for defining data sources model."""

import enum
from datetime import datetime

from sqlalchemy import JSON, TIMESTAMP, Boolean, Column, Enum, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.utils.utils import generate_uuid


class ProcessStatus(enum.Enum):
    """Represents a process_status enum."""

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8


class DataSources(Base):
    """Represents a data_sources model."""

    __tablename__ = "data_sources"
    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    type = Column(String)
    description = Column(String, nullable=True)
    user_id = Column(String, ForeignKey("users.id"))
    data = Column(String, nullable=True)
    cleaning_suggestions = Column(JSON, nullable=True)
    name = Column(String, nullable=True)
    process_status = Column(Enum(ProcessStatus))
    data_dictionary = Column(JSON, nullable=True)
    is_selected = Column(Boolean)
    is_archived = Column(Boolean, default=False)
    celery_task_id = Column(String, nullable=True)
    data_features = Column(JSON, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    modified_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)

    # Add a one-to-many relationship between data_sources and conversations

    conversation = relationship("Conversations", back_populates="data_sources")

    # Define many-to-one relationship with Users
    user = relationship("Users", back_populates="data_sources")
