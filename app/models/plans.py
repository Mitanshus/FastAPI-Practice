"""Import necessary modules for defining plans model."""

import enum

from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.utils.utils import generate_uuid


class PlanCategory(enum.Enum):
    """Represents a plan category enum."""

    FREE = "free"
    PAID = "paid"


class Plans(Base):
    """Represents a plans model."""

    __tablename__ = "plans"

    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    credits = Column(Integer, nullable=True)
    duration = Column(String, nullable=True)
    price = Column(Integer, nullable=True)
    category = Column(Enum(PlanCategory), nullable=True)

    # Define one-to-many relationship with Transactions
    transactions = relationship("Transactions", back_populates="plan")
