from sqlalchemy.orm import relationship

from backend.database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Payment_Method(Base):
    __tablename__ = "payment_method"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)


    user = relationship("User", back_populates="payment_methods")
    payments = relationship("Payment", back_populates="payment_method")
