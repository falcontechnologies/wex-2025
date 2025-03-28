# This program creates a SQLite database to manage:
# - Users
# - Subscriptions
# - Payment Methods
# - Transaction History

# Author: aaronqwang
# Date: March 4th, 2025
# Edited to Fit SQLAlchemy by Ming Qian Gao
# Edited Date: March, 23rd, 2025

# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Define the base class for declarative class definitions
Base = declarative_base()

# Define the User table
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    phone_number = Column(String)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP')
    last_login = Column(DateTime)

    # Define relationships
    subscriptions = relationship("Subscription", back_populates="user")
    payment_methods = relationship("PaymentMethod", back_populates="user")

# Define the Subscription table
class Subscription(Base):
    __tablename__ = 'subscription'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    name = Column(String)
    service_provider = Column(String)
    start_date = Column(DateTime, nullable=False)
    expiry_date = Column(DateTime)
    is_trial = Column(Integer, CheckConstraint('is_trial IN (0,1)'), nullable=False)
    is_recurring = Column(Integer, CheckConstraint('is_recurring IN (0,1)'), nullable=False)
    payment_frequency = Column(String, nullable=False)
    cost = Column(Float)
    status = Column(String, nullable=False)
    subscription_type = Column(String)
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP')

    # Define relationships
    user = relationship("User", back_populates="subscriptions")
    transactions = relationship("TransactionHistory", back_populates="subscription")

# Define the PaymentMethod table
class PaymentMethod(Base):
    __tablename__ = 'payment_method'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    type = Column(String)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))

    # Define relationships
    user = relationship("User", back_populates="payment_methods")
    transactions = relationship("TransactionHistory", back_populates="payment_method")

# Define the TransactionHistory table
class TransactionHistory(Base):
    __tablename__ = 'transaction_history'
    id = Column(Integer, primary_key=True, autoincrement=True)
    subscription_id = Column(Integer, ForeignKey('subscription.id', ondelete='CASCADE'))
    payment_id = Column(Integer, ForeignKey('payment_method.id', ondelete='CASCADE'))
    amount_paid = Column(Float, nullable=False)
    date_paid = Column(DateTime, default='CURRENT_TIMESTAMP')

    # Define relationships
    subscription = relationship("Subscription", back_populates="transactions")
    payment_method = relationship("PaymentMethod", back_populates="transactions")

# Create an engine that stores data in the local directory's customer.db file
engine = create_engine('sqlite:///customer.db')

# Create all tables by issuing CREATE TABLE commands to the database
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()