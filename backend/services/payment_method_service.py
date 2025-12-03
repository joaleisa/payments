from backend.models.payment_method import PaymentMethod
from backend.repositories.payment_method_repository import PaymentMethodRepository
from backend.schemas.payment_method_schema import *


class PaymentMethodService:
    def __init__(self, repository: PaymentMethodRepository):
        self.repository = repository

    def create_payment_method(self, payment_method_data: PaymentMethodCreate) -> PaymentMethod:
        new_payment_method = PaymentMethod(**payment_method_data.dict())
        return self.repository.create(new_payment_method)