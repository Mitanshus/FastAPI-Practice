"""Import necessary modules for defining webhooks model."""

from sqlalchemy import JSON, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.utils.utils import generate_uuid


class WebHooks(Base):
    """Represents a webhooks model."""

    __tablename__ = "webhooks"
    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    event_id = Column(String, nullable=True)
    event = Column(JSON, nullable=True)
    transaction_id = Column(String, ForeignKey("transactions.id"))

    transaction = relationship("Transactions", back_populates="webhook")
