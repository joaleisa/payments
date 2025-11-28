from datetime import timedelta

from backend.models import Installment
from backend.models.payment import Payment
from backend.repositories.installment_repository import Installment_Repository
from backend.repositories.payment_repository import Payment_Repository
from backend.schemas.payment_schema import *

class Payment_Service:
    def __init__(self, repository: Payment_Repository, installment_repository: Installment_Repository):
        self.repository = repository
        self.installment_repository = installment_repository

    def create_payment(self, payment_data: PaymentCreate) -> Payment:
        new_payment = Payment(**payment_data.dict())
        created_payment = self.repository.create(new_payment)

        print("LLEGO")
        amount_per_installment = created_payment.total_amount / created_payment.installment_qty

        for i in range(created_payment.installment_qty):
            due_date = payment_data.first_payment_date + timedelta(days=i*30) #todo: checkear dias

            installment_i = Installment(
                payment_id = created_payment.id,
                installment_number = i+1,
                amount = amount_per_installment,
                due_date = due_date,
                is_paid = False #todo: check this
            )

            self.installment_repository.create(installment_i)

        return created_payment


        #todo:
        # installment_service.service_installments(payment_created)
        # return payment_created