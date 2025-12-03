from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from backend.database.database import get_db
from backend.repositories.installment_repository import InstallmentRepository
from backend.repositories.purchase_repository import PurchaseRepository
from backend.schemas.purchase_schema import *
from backend.services.purchase_service import PurchaseService

router = APIRouter(
    prefix="/purchase",
    tags=["purchase"]
)

def get_purchase_service(db: Session = Depends(get_db)) -> PurchaseService:
    purchase_repository = PurchaseRepository(db)
    return PurchaseService(purchase_repository)

@router.post("/", status_code=status.HTTP_201_CREATED)  # todo: response model
def create_purchase(purchase: PurchaseCreate, service: PurchaseService = Depends(get_purchase_service)):
    return service.create_purchase(purchase)