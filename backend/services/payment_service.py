from backend.models.payment import Payment
from backend.repositories.payment_repository import Payment_Repository
from backend.schemas.payment_schema import *

class Payment_Service:
    def __init__(self, repository: Payment_Repository):
        self.repository = repository

    def create_payment(self, payment_data: PaymentCreate) -> Payment:
        new_payment = Payment(**payment_data.dict())
        return self.repository.create(new_payment)

        #todo:
        # installment_service.service_installments(payment_created)
        # return payment_created