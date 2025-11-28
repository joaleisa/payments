from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from backend.database.database import get_db
from backend.models.person import Person
from backend.repositories.person_repository import PersonRepository
from backend.schemas.person_schema import *
from backend.services.person_service import PersonService

router = APIRouter(
    prefix="/person",
    tags=["person"]
)
def get_person_service(db: Session = Depends(get_db)) -> PersonService:
    repository = PersonRepository(db)
    return PersonService(repository)

@router.post("/", response_model=PersonResponse)
#1 modelo, 2 servicio(repositorio)
def create_person(person: PersonCreate, service: PersonService = Depends(get_person_service)):
    return service.create_person(person)

