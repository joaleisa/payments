from sqlalchemy import Column, Integer, String

from backend.database.database import Base

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(45), nullable=False)


    #todo: verificar con modelos POO
    