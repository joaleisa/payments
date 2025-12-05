import datetime
from typing import Optional
from pydantic import BaseModel

class PurchaseCreate(BaseModel):
    payment_method_id: int
    user_id: int
    description: str | None = None
    created_at: datetime.date | None = None
    installment_qty: int | None = 1
    first_payment_date: datetime.date | None = datetime.date.today()
    total_amount: float
    person_ids: list[int]

class PurchaseUpdate(BaseModel):
    id: int
    payment_method_id: int | None
    description: Optional[str] = None

class PurchaseResponse(BaseModel):
    id: int
    payment_method_id: int
    # person_id: int
    description: Optional[str] = None
    total_amount: float

