from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, DATE
from sqlalchemy.orm import relationship
from backend.database.database import Base

class Installment_Share(Base):
    __tablename__ = "installment_share"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    installment_id = Column(Integer, ForeignKey("installment.id"), nullable=False)
    person_id = Column(Integer, ForeignKey("person.id"), nullable=False)
    is_paid = Column(Boolean, default=False)
    paid_date = Column(DATE, nullable=True)
    notes = Column(String(255), nullable=True)

    installment = relationship("Installment", back_populates="installment_shares")