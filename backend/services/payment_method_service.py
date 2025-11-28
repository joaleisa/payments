from backend.models.payment_method import Payment_Method
from backend.repositories.payment_method_repository import Payment_Method_Repository
from backend.schemas.payment_method_schema import *


class Payment_Method_Service:
    def __init__(self, repository: Payment_Method_Repository):
        self.repository = repository

    def create_payment_method(self, payment_method_data: PaymentMethodCreate) -> Payment_Method:
        new_payment_method = Payment_Method(**payment_method_data.dict())
        return self.repository.create(new_payment_method)