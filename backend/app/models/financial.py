from sqlalchemy import Column, String, Numeric, Date, ForeignKey, Text, Enum, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.types import TypeDecorator, VARCHAR
import enum
from decimal import Decimal
from .base import BaseModel

class TransactionType(enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"

class Currency(TypeDecorator):
    """Custom type for handling currency with proper precision"""
    impl = VARCHAR
    cache_ok = True
    
    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(VARCHAR(20))

class BankAccount(BaseModel):
    __tablename__ = "bank_accounts"
    
    user_id = Column(ForeignKey("users.id"), nullable=False)
    account_name = Column(String, nullable=False)
    account_number = Column(String, nullable=True)  # Last 4 digits only
    bank_name = Column(String, nullable=True)
    account_type = Column(String, nullable=True)  # checking, savings, etc.
    
    # Relationships
    user = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")

class Category(BaseModel):
    __tablename__ = "categories"
    
    name = Column(String, nullable=False, unique=True)
    description = Column(Text, nullable=True)
    color = Column(String(7), nullable=True)  # Hex color code
    icon = Column(String, nullable=True)
    is_default = Column(Boolean, default=False)
    
    # Relationships
    transactions = relationship("Transaction", back_populates="category")

class Transaction(BaseModel):
    __tablename__ = "transactions"
    
    user_id = Column(ForeignKey("users.id"), nullable=False)
    account_id = Column(ForeignKey("bank_accounts.id"), nullable=False)
    category_id = Column(ForeignKey("categories.id"), nullable=True)
    
    # Transaction details
    date = Column(Date, nullable=False)
    amount = Column(Numeric(precision=10, scale=2), nullable=False)
    description = Column(Text, nullable=False)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    
    # Additional fields
    original_description = Column(Text, nullable=True)  # Original from bank
    notes = Column(Text, nullable=True)  # User notes
    
    # Relationships
    user = relationship("User", back_populates="transactions")
    account = relationship("BankAccount", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")