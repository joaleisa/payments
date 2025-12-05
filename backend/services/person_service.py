from fastapi import HTTPException, status
from unicodedata import normalize

from backend.models.person import Person
from backend.repositories.person_repository import PersonRepository
from backend.schemas.person_schema import *

class PersonService:
    def __init__(self, repository: PersonRepository):
        self.repository = repository

    def create_person(self, person_data: PersonCreate) -> Person:
        #todo: las personas deberían estar asociadas a un usuario
        # new_person = Person(**person_data.dict())
        new_person = Person(
            name=person_data.name,
            user_id=person_data.user_id
        )
        return self.repository.create(new_person)

    def get_all(self):
        persons = self.repository.get_all()
        if not persons:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay personas registradas")
        return persons

    def get_by_id(self, person_id):
        person = self.repository.get_by_id(person_id)
        if not person:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Persona no encontrada")
        return person

    def get_by_user_id(self, user_id):
        persons = self.repository.get_by_user_id(user_id)
        if not persons:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="No hay una persona asociada a ese usuario")
        return persons

    def get_by_name(self, name):
        persons = self.repository.get_by_name(name)
        if not persons:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay ninguna persona con ese nombre")
        return persons

    def update_person(self, person_id, person):
        #1 get person
        db_person = self.get_by_id(person_id)
        if not db_person:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Persona no encontrada")
        #2 get update dict
        update_data = person.dict(exclude_unset=True)
        #3 update person with the dict
        for field, value in update_data.items():
            setattr(db_person, field, value)

        self.repository.update(db_person)
        return db_person
