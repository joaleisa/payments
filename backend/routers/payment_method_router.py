from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from backend.database.database import get_db
from backend.models.payment_method import Payment_Method
from backend.repositories.payment_method_repository import Payment_Method_Repository
from backend.schemas.payment_method_schema import *
from backend.services.payment_method_service import Payment_Method_Service

router = APIRouter(
    prefix="/payment_method",
    tags=["payment_method"]
)

def get_payment_method_service(db: Session = Depends(get_db)) -> Payment_Method_Service:
    repository = Payment_Method_Repository(db)
    return Payment_Method_Service(repository)

@router.post("/", response_model=PaymentMethodResponse, status_code=status.HTTP_201_CREATED)
def create_payment_method(payment_method: PaymentMethodCreate, service: Payment_Method_Service = Depends(get_payment_method_service)):
    return service.create_payment_method(payment_method)
