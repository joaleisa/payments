from sqlalchemy.orm import Session
from backend.models.purchase import Purchase

class Purchase_Repository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, payment: Purchase) -> Purchase:
        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)
        return payment