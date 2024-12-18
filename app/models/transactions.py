"""Import necessary modules for defining transactions model."""

import enum
from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.utils.utils import generate_uuid


class TransactionStatus(enum.Enum):
    """Represents a transaction status enum."""

    PENDING = "pending"
    SUCCESS = "success"
    FAILURE = "failure"


class Transactions(Base):
    """Represents a transactions model."""

    __tablename__ = "transactions"
    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"))
    plan_id = Column(String, ForeignKey("plans.id"))
    purchased_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    status = Column(Enum(TransactionStatus), nullable=True)
    external_order_id = Column(String, nullable=True)
    amount = Column(Integer, nullable=True)
    currency = Column(String, nullable=True)
    payment_id = Column(String, nullable=True)
    signature = Column(String, nullable=True)
    receipt = Column(String, unique=True, nullable=True)

    # Define one-to-one relationship with CreditLedgers
    credit_ledger = relationship(
        "CreditLedgers", uselist=False, back_populates="transaction"
    )

    # Define one-to-one relationship with WebHooks (assuming each transaction has one Razorpay
    # webhook)
    webhook = relationship("WebHooks", uselist=False, back_populates="transaction")

    # Define many-to-one relationship with Plans
    plan = relationship("Plans", back_populates="transactions")

    user = relationship("Users", back_populates="transactions")
