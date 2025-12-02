from sqlalchemy.orm import relationship

from backend.database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DATE, Boolean
import datetime

class Installment(Base):
    __tablename__ = "installment"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    purchase_id = Column(Integer, ForeignKey("purchase.id"), nullable=False)
    installment_number = Column(Integer, nullable=False)
    amount = Column(DECIMAL(10,2), nullable=False)
    due_date = Column(DATE, nullable=True)
    is_paid = Column(Boolean, default=False)
    paid_date = Column(DATE, nullable=True)

    purchase = relationship("Purchase", back_populates="installments")
