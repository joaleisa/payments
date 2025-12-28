from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session, defer

from backend.database.database import get_db
from backend.repositories.user_repository import UserRepository
from backend.services.user_service import UserService
from backend.schemas.user_schema import UserResponse, UserCreate


router = APIRouter(prefix="/user", tags=["user"])


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repository = UserRepository(db)
    return UserService(repository)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
async def get_all_users(service: UserService = Depends(get_user_service)):
    return service.get_all_users()

@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get_by_id(user_id)

#todo: resto de métodos