from backend.models.installment_share import InstallmentShare
from backend.repositories.installment_share_repository import InstallmentShareRepository
from backend.schemas.installment_share_schema import *

class InstallmentShareService:
    def __init__(self, repository: InstallmentShareRepository):
        self.repository = repository

