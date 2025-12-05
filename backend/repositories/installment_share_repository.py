from sqlalchemy.orm import Session

class InstallmentShareRepository:
    def __init__(self, db: Session):
        self.db = db

