import datetime
from typing import Optional

from pydantic import BaseModel

class PaymentCreate(BaseModel):
    payment_method_id: int
    user_id: int
    person_id: int #todo: list and create table persons_payments
    description: Optional[str] = None
    created_at: Optional[datetime.date] = None
    installment_qty: Optional[int] = None
    first_payment_date: Optional[datetime.date] = None
    total_amount: float

class PaymentUpdate(BaseModel):
    payment_method_id: int
    person_id: int
    description: Optional[str] = None

class PaymentResponse(BaseModel):
    id: int
    payment_method_id: int
    person_id: int
    description: Optional[str] = None
    total_amount: float
