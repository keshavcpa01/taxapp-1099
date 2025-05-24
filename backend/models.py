from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    submissions = relationship("Submission", back_populates="owner")

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    payer_name = Column(String)
    payer_tin = Column(String)
    payer_address = Column(String)
    payer_city = Column(String)
    payer_state = Column(String)
    payer_zip = Column(String)
    payer_email = Column(String)
    recipient_name = Column(String)
    recipient_tin = Column(String)
    recipient_phone = Column(String)
    recipient_address = Column(String)
    recipient_city = Column(String)
    recipient_state = Column(String)
    recipient_zip = Column(String)
    payment_date = Column(String)
    nonemployee_compensation = Column(String)
    federal_income_tax_withheld = Column(String)
    state = Column(String)
    state_id = Column(String)
    state_income = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    owner = relationship("User", back_populates="submissions")
