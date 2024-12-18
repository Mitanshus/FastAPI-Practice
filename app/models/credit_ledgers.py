"""Import necessary modules for defining credit ledgers model."""

import enum
from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.utils.utils import generate_uuid


class CreditLedgerPriority(enum.Enum):
    """Represents a credit ledger priority enum."""

    HIGH = "1"
    LOW = "0"


class CreditLedgers(Base):
    """Represents a credit_ledgers model."""

    __tablename__ = "credit_ledgers"
    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"))
    total_credits = Column(Integer, nullable=True)
    available_credits = Column(Integer, nullable=True)
    transaction_id = Column(String, ForeignKey("transactions.id"))
    priority = Column(Enum(CreditLedgerPriority), nullable=True)
    expiry_date = Column(DateTime, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)

    # transaction = relationship("Transactions", back_populates="credit_ledger")

    # Define many-to-one relationship with Users
    user = relationship("Users", back_populates="credit_ledgers")

    # Define one-to-one relationship with Transactions
    transaction = relationship(
        "Transactions", uselist=False, back_populates="credit_ledger"
    )
