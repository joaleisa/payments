from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from backend.database.database import get_db
from backend.models.payment import Payment
from backend.repositories.installment_repository import Installment_Repository
from backend.repositories.payment_repository import Payment_Repository
from backend.schemas.payment_schema import *
from backend.services.payment_service import Payment_Service
from backend.services.installment_service import Installment_Service

router = APIRouter(
    prefix="/payment",
    tags=["payment"]
)

def get_payment_service(db: Session = Depends(get_db)) -> Payment_Service:
    payment_repository = Payment_Repository(db)
    installment_repository = Installment_Repository(db)
    return Payment_Service(payment_repository, installment_repository)

@router.post("/", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def create_payment(payment: PaymentCreate, service: Payment_Service = Depends(get_payment_service)):
    return service.create_payment(payment)