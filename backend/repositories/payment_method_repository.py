from sqlalchemy.orm import Session
from backend.models.payment_method import PaymentMethod


class PaymentMethodRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, payment_method: PaymentMethod) -> PaymentMethod:
        self.db.add(payment_method)
        self.db.commit()
        self.db.refresh(payment_method)
        return payment_method