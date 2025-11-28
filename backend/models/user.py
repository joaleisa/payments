import datetime

from sqlalchemy.orm import relationship
from backend.database.database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(45), nullable=False, unique=True)
    role = Column(String(45), nullable=False, default="user")
    create_at = Column(String(45), nullable=False, default=datetime.date.today())
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)


    payment_methods = relationship("Payment_Method", back_populates="user")
