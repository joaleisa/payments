from backend.models.installment import Installment
from backend.repositories.installment_repository import InstallmentRepository
from backend.schemas.installment_schema import *


class InstallmentService:
    def __init__(self, repository: InstallmentRepository):
        self.repository = repository

    def create_installment(self, installment_data: InstallmentCreate) -> Installment:
        new_installment = Installment(**installment_data.dict())
        return self.repository.create(new_installment)