from datetime import datetime
from .database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    submissions = relationship("Submission", back_populates="owner")

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True)
    payer_name = Column(String)
    recipient_name = Column(String)
    amount = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    owner = relationship("User", back_populates="submissions")
