from backend.models.installment_share import Installment_Share
from backend.repositories.installment_share_repository import Installment_Share_Repository
from backend.schemas.installment_share_schema import *

class Installment_Share_Service:
    def __init__(self, repository: Installment_Share_Repository):
        self.repository = repository

