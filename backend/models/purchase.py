import datetime
from backend.database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DATE
from sqlalchemy.orm import relationship

class Purchase(Base):
    __tablename__ = "purchase"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    payment_method_id = Column(Integer, ForeignKey("payment_method.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    description = Column(String(255), nullable=False)
    created_at = Column(DATE, nullable=False, default=datetime.date.today())
    installment_qty = Column(Integer, nullable=False, default=1)
    first_payment_date = Column(DATE, default=datetime.date.today()) #todo: checkear formato en bd
    total_amount = Column(DECIMAL(10,2), nullable=False)


    user = relationship("User", back_populates="purchases")
    payment_method = relationship("PaymentMethod", back_populates="purchases")
    installments = relationship("Installment", back_populates="purchase")