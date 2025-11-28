from backend.models.installment import Installment
from backend.repositories.installment_repository import Installment_Repository
from backend.schemas.installment_schema import *


class Installment_Service:
    def __init__(self, repository: Installment_Repository):
        self.repository = repository

    def create_installment(self, installment_data: InstallmentCreate) -> Installment:
        new_installment = Installment(**installment_data.dict())
        return self.repository.create(new_installment)