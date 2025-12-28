import datetime

from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import relationship
from backend.database.database import Base
from sqlalchemy import Column, Integer, String

# from backend.models.person import Person


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(45), nullable=False, unique=True)
    role = Column(String(45), nullable=False, default="user")
    created_at = Column(DATETIME, nullable=False, default=datetime.datetime.today()) #todo: only default
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)


    payment_methods = relationship("PaymentMethod", back_populates="user")
    persons = relationship("Person", back_populates="user")
    purchases = relationship("Purchase", back_populates="user")