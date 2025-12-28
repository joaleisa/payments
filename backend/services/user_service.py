from fastapi import HTTPException, status
from passlib.context import CryptContext

from backend.models.user import User
from backend.repositories.user_repository import UserRepository
from backend.schemas.user_schema import *

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user_data: UserCreate) -> User:

        #Todo: create corresponding person to this user
        if self.repository.get_by_email(user_data.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este email ya está asociado a otra cuenta"
            )

        if self.repository.get_by_username(user_data.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Usuario no disponible"
            )

        # Business logic: hash password

        print("LLEGA AL HASH")
        hashed_password = password_context.hash(user_data.password)
        new_user = User(
            username=user_data.username,
            email=user_data.email,
            password=hashed_password
        )

        return self.repository.create(new_user)