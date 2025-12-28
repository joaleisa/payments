from fastapi import APIRouter, Depends, HTTPException, status
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

@router.post("/", response_model=PersonResponse, status_code=status.HTTP_201_CREATED)
#1 modelo, 2 servicio(repositorio)
def create_person(person: PersonCreate, service: PersonService = Depends(get_person_service)):
    return service.create_person(person)

@router.get("/", response_model=list[PersonResponse], status_code=status.HTTP_200_OK)
def get_all_persons(service: PersonService = Depends(get_person_service)):
    return service.get_all()

@router.get("/{person_id}", response_model=PersonResponse, status_code=status.HTTP_200_OK)
def get_person(person_id: int ,service: PersonService = Depends(get_person_service)): # ToDo: fix
    return service.get_by_id(person_id)

@router.get("/name/{name}", response_model=list[PersonResponse], status_code=status.HTTP_200_OK)
def get_person_by_name(name: str, service: PersonService = Depends(get_person_service)):
    #persons with a name containing {name}
    return service.get_by_name(name)


@router.get("/user/{user_id}", response_model=list[PersonResponse], status_code=status.HTTP_200_OK)
def get_person_by_user_id(user_id: int, service: PersonService = Depends(get_person_service)):
    return service.get_by_user_id(user_id)

@router.put("/{person_id}", response_model=PersonResponse, status_code=status.HTTP_200_OK)
def update_person(person_id: int, person: PersonUpdateName, service: PersonService = Depends(get_person_service)):
    return service.update_person(person_id, person)

