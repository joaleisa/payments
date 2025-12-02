from pydantic import BaseModel

class InstallmentShareCreate(BaseModel):
    installment_id: int
    person_id: int
    share_amount: float