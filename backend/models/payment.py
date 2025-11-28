import datetime
from backend.database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DATE
from sqlalchemy.orm import relationship

class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    payment_method_id = Column(Integer, ForeignKey("payment_method.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    #todo: listado de personas
    person_id = Column(Integer, ForeignKey("person.id"), nullable=False)
    description = Column(String(255), nullable=False)
    created_at = Column(DATE, nullable=False, default=datetime.date.today())
    installment_qty = Column(Integer, nullable=False, default=1)
    first_payment_date = Column(String(45), nullable=False, default=datetime.date.today())
    total_amount = Column(DECIMAL(10,2), nullable=False)


    user = relationship("User", back_populates="payments")
    payment_method = relationship("Payment_Method", back_populates="payments")
    person = relationship("Person", back_populates="payments") #todo: modificar para muchas personas
    # installments = relationship("Installment", back_populates="payment")