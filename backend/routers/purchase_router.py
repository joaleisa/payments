from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from backend.database.database import get_db
from backend.repositories.installment_repository import Installment_Repository
from backend.repositories.purchase_repository import Purchase_Repository
from backend.schemas.purchase_schema import *
from backend.services.purchase_service import Purchase_Service

router = APIRouter(
    prefix="/purchase",
    tags=["purchase"]
)

def get_purchase_service(db: Session = Depends(get_db)) -> Purchase_Service:
    purchase_repository = Purchase_Repository(db)
    installment_repository = Installment_Repository(db)
    return Purchase_Service(purchase_repository, installment_repository)

@router.post("/", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def create_purchase(purchase: PurchaseCreate, service: Purchase_Service = Depends(get_purchase_service)):
    return service.create_purchase(purchase)