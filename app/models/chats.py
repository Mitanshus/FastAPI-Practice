"""Import necessary modules for defining chats model."""

import enum
from datetime import datetime

from sqlalchemy import JSON, TIMESTAMP, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.utils.utils import generate_uuid


class GenRPTStatusCode(enum.Enum):
    """Represents a genrpt_status_code enum."""

    PROCESS_INITIALIZED = 0
    FORMATTED_QUESTION = 1
    RESPONSE_TYPE_DETERMINATION = 2
    QUERY_GENERATION = 3
    OUTPUT_PARSING = 4


class GenRPTErrorCode(enum.Enum):
    """Represents a genrpt_error_code enum."""

    NO_ERROR = 0
    FORMATTED_QUESTION_FAILURE = 1
    RESPONSE_TYPE_DETERMINATION_ERROR = 2
    QUERY_GENERATION_FAILURE = 3
    OUTPUT_PARSING_ERROR = 4


class Chats(Base):
    """Represents a chats model within a conversation."""

    __tablename__ = "chats"
    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"))
    genrpt_status_code = Column(Enum(GenRPTStatusCode), nullable=True)
    genrpt_error_code = Column(Enum(GenRPTErrorCode), nullable=True)
    conv_id = Column(
        String,
        ForeignKey("conversations.id"),
        nullable=True,
    )  # nullable foreign key
    question = Column(String)
    sql = Column(String, nullable=True)
    response = Column(String, nullable=True)
    sig_response = Column(String, nullable=True)
    type = Column(Integer, nullable=True)
    context_id = Column(String, ForeignKey("contexts.id"))
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    token_count = Column(JSON, nullable=True)

    # Add a many-to-one relationship from Chats to Conversations
    conversation = relationship("Conversations", back_populates="chats")

    # Add a many-to-one relationship from Chats to Contexts
    context = relationship("Contexts", back_populates="chats")
