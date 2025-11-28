from fastapi import HTTPException, status

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