from sqlalchemy.orm import Session
from backend.models.person import Person

class PersonRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, person: Person) -> Person:
        self.db.add(person)
        self.db.commit()
        self.db.refresh(person)
        return person