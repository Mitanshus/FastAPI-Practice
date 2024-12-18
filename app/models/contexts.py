"""Import necessary modules for defining contexts model."""

from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.utils.utils import generate_uuid


class Contexts(Base):
    """Represents a contexts model."""

    __tablename__ = "contexts"
    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"))
    conversation_id = Column(String, ForeignKey("conversations.id"))
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)

    # Add a one-to-many relationship between Context and Chats
    chats = relationship("Chats", back_populates="context")

    # Add a many-to-one relationship between Context and Conversations
    conversation = relationship("Conversations", back_populates="contexts")
