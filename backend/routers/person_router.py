from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from backend.database.database import get_db
from backend.models.person import Person
from backend.schemas.person_schema import PersonCreate, PersonResponse

router = APIRouter(
    prefix="/person",
    tags=["person"]
)


@router.post("/", response_model=PersonResponse)
def create_person(person: PersonCreate, db: Session = Depends(get_db)):
    #todo: mover al service
    db_person = Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person