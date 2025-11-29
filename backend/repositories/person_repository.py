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

    def get_all(self):
        persons = self.db.query(Person).offset(0).limit(100).all()
        return persons

    def get_by_id(self, person_id: int):
        return self.db.query(Person).filter(Person.id == person_id).first()

    def get_by_user_id(self, user_id):
        return self.db.query(Person).filter(Person.user_id == user_id).offset(0).limit(100).all()

    def get_by_name(self, name):
        return self.db.query(Person).filter(Person.name.contains(name)).offset(0).limit(100).all()

    def update(self, person: Person):
        self.db.add(person)
        self.db.commit()
        self.db.refresh(person)
        return person