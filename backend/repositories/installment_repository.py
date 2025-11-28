from sqlalchemy.orm import Session

from backend.models import Installment
from backend.models.payment_method import Payment_Method

class Installment_Repository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, installment: Installment) -> Installment:
        self.db.add(installment)
        self.db.commit()
        self.db.refresh(installment)
        return installment