from sqlalchemy.orm import Session
from backend.models.payment_method import Payment_Method


class Payment_Method_Repository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, payment_method: Payment_Method) -> Payment_Method:
        self.db.add(payment_method)
        self.db.commit()
        self.db.refresh(payment_method)
        return payment_method