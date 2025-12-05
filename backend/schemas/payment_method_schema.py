from pydantic import BaseModel


class PaymentMethodCreate(BaseModel):
    name: str
    user_id: int




class PaymentMethodResponse(BaseModel):
    id: int
    name: str



