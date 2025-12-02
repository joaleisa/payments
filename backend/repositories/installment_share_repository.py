from sqlalchemy.orm import Session
from backend.models.installment_share import Installment_Share

class Installment_Share_Repository:
    def __init__(self, db: Session):
        self.db = db

