"""Import necessary modules for defining users model."""

from datetime import datetime

from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.utils.utils import generate_uuid


class Users(Base):
    """Represents a users model."""

    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    email = Column(String, unique=True)
    username = Column(String)
    password_hash = Column(String)
    role = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    modified_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    is_active = Column(Integer, default=1)
    phone_number = Column(String, unique=True)
    company_name = Column(String)
    is_trial = Column(Boolean, default=1)
    country_code = Column(String)

    # Define one-to-many relationship with DataSources
    data_sources = relationship("DataSources", back_populates="user")

    # Define one-to-many relationship with CreditLedgers
    credit_ledgers = relationship("CreditLedgers", back_populates="user")

    # Define one-to-many relationship with Transactions
    transactions = relationship("Transactions", back_populates="user")
