import datetime
from typing import Optional

from pydantic import BaseModel

class InstallmentCreate(BaseModel):
    payment_id: int
    installment_number: int
    amount: float
    due_date: datetime.date
    is_paid: bool
    paid_date: Optional[datetime.date] = None
