from datetime import timedelta

from backend.models import Installment
from backend.models.installment_share import InstallmentShare
from backend.models.purchase import Purchase
from backend.repositories.installment_repository import InstallmentRepository
from backend.repositories.purchase_repository import PurchaseRepository
from backend.schemas.purchase_schema import *

class PurchaseService:
    def __init__(self, repository: PurchaseRepository):
        self.repository = repository


    def create_purchase(self, purchase_data: PurchaseCreate) -> Purchase:  # todo: syntax
        """
        This method creates a purchase, its installments and the share for each installment.
        The goal is to abort the entire purchase if something goes wrong. Basically all or nothing.
        """
        try:
            new_purchase = Purchase(
                payment_method_id=purchase_data.payment_method_id,
                user_id=purchase_data.user_id,
                description=purchase_data.description,
                created_at=purchase_data.created_at,
                installment_qty=purchase_data.installment_qty,
                first_payment_date=purchase_data.first_payment_date,
                total_amount=purchase_data.total_amount
            )

            self.repository.db.add(new_purchase)
            self.repository.db.flush()  # todo: what's the flush for?

            for i in range(new_purchase.installment_qty):
                current_installment = Installment(
                    purchase_id=new_purchase.id,
                    installment_number= i + 1,
                    amount = new_purchase.total_amount / new_purchase.installment_qty,
                    due_date = new_purchase.first_payment_date + timedelta(days=i * 30),
                    is_paid = False
                )

                self.repository.db.add(current_installment)  # todo: make the installment_repository save it?
                self.repository.db.flush()

                for person_id in purchase_data.person_ids:  # notice that we use purchase_data instead of new_purchase
                    installment_share = InstallmentShare(
                        installment_id=current_installment.id,
                        person_id= person_id,
                        is_paid = False,
                        amount = current_installment.amount / len(purchase_data.person_ids),
                    )
                    self.repository.db.add(installment_share)

            self.repository.db.commit()
            return new_purchase

        except Exception as e:
            self.repository.db.rollback()
            raise e

    def update_purchase(self, purchase: Purchase):
        pass

    def get_by_id(self, purchase_id):
        return self.repository.get_by_id(purchase_id)

    def get_all(self):
        return self.repository.get_all()