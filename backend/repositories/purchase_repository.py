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

    def get_by_id(self, purchase_id):
        return self.db.query(Purchase).filter(Purchase.id == purchase_id).first()

    def get_all(self):
        return self.db.query(Purchase).offset(0).limit(100).all()

