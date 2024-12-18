"""Import necessary modules for defining conversations model."""

from datetime import datetime

from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.utils.utils import generate_uuid


class Conversations(Base):
    """Represents a conversations model."""

    __tablename__ = "conversations"
    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"))
    name = Column(String, default="New conversation")
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    is_archived = Column(Boolean, default=False)
    data_source_id = Column(String, ForeignKey("data_sources.id"))

    # Add a one-to-many relationship between Conversations and Chats
    chats = relationship("Chats", back_populates="conversation")

    # Add a one-to-many relationship between Conversations and Contexts
    contexts = relationship("Contexts", back_populates="conversation")

    # Add a many-to-one relationship between Conversations and data_sources
    data_sources = relationship("DataSources", back_populates="conversation")
