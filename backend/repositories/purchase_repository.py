from sqlalchemy.orm import Session
from backend.models.purchase import Purchase

class PurchaseRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, payment: Purchase) -> Purchase:
        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)
        return payment