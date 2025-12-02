import datetime
from typing import Optional

from pydantic import BaseModel

class PurchaseCreate(BaseModel):
    payment_method_id: int
    user_id: int
    person_id: list[int]
    description: Optional[str] = None
    created_at: Optional[datetime.date] = None
    installment_qty: Optional[int] = None
    first_payment_date: Optional[datetime.date] = datetime.date.today()
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
