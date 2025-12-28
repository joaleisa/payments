from fastapi import HTTPException, status
from passlib.context import CryptContext

from backend.models import Person
from backend.models.user import User
from backend.repositories.user_repository import UserRepository
from backend.schemas.user_schema import *

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user_data: UserCreate) -> User:
        # ToDo: refactor code. Too much responsibilities for this one method
        try:
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

            hashed_password = password_context.hash(user_data.password)
            new_user = User(
                username=user_data.username,
                email=user_data.email,
                password=hashed_password
            )

            self.repository.db.add(new_user)
            self.repository.db.flush()

            new_person = Person(
                name = user_data.username,
                user_id = new_user.id
            )
            self.repository.db.add(new_person)

            self.repository.db.commit()
            return new_user

        except Exception as e:
            self.repository.db.rollback()
            raise e

    def get_users(self) -> list[User]:
        return self.repository.get_users()

    def get_user(self, user_id):
        return self.repository.get_by_id(user_id)