from datetime import timedelta

from backend.models import Installment
from backend.models.purchase import Purchase
from backend.repositories.installment_repository import Installment_Repository
from backend.repositories.purchase_repository import Purchase_Repository
from backend.schemas.purchase_schema import *

class Purchase_Service:
    def __init__(self, repository: Purchase_Repository, installment_repository: Installment_Repository):
        self.repository = repository
        self.installment_repository = installment_repository

    def create_purchase(self, purchase_data: PurchaseCreate) -> Purchase:
        new_purchase = Purchase(**purchase_data.dict())
        created_purchase = self.repository.create(new_purchase)

        print("LLEGO")
        amount_per_installment = created_purchase.total_amount / created_purchase.installment_qty

        for i in range(created_purchase.installment_qty):
            due_date = purchase_data.first_payment_date + timedelta(days=i*30) #todo: checkear dias

            installment_i = Installment(
                purchase_id = created_purchase.id,
                installment_number = i+1,
                amount = amount_per_installment,
                due_date = due_date,
                is_paid = False #todo: check this
            )

            self.installment_repository.create(installment_i)

        return created_purchase


        #todo:
        # installment_service.service_installments(payment_created)
        # return payment_created