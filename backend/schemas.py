from pydantic import BaseModel, EmailStr
from typing import Optional
from decimal import Decimal
from datetime import date

class UserCreate(BaseModel):
    username: str
    password: str


class SubmissionCreate(BaseModel):
    payer_name: str
    payer_tin: str
    payer_address: str
    payer_city: str
    payer_state: str
    payer_zip: str
    payer_email: EmailStr

    recipient_name: str
    recipient_tin: str
    recipient_phone: str
    recipient_address: str
    recipient_city: str
    recipient_state: str
    recipient_zip: str

    payment_date: date
    nonemployee_compensation: Decimal
    federal_income_tax_withheld: Decimal

    state: str
    state_id: str
    state_income: Decimal

class SubmissionOut(SubmissionCreate):
    id: int
    user_id: int
    created_at: date

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

