from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.database.database import Base


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)


    user = relationship("User", back_populates="persons")
    #todo: verificar con modelos POO
    