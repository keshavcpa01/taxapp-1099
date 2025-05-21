from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SubmissionCreate(BaseModel):
    payer_name: str
    recipient_name: str
    amount: str

class SubmissionOut(SubmissionCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
