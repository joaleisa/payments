from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from backend.database.database import get_db
from backend.models.payment_method import PaymentMethod
from backend.repositories.payment_method_repository import PaymentMethodRepository
from backend.schemas.payment_method_schema import *
from backend.services.payment_method_service import PaymentMethodService

router = APIRouter(
    prefix="/payment_method",
    tags=["payment_method"]
)

def get_payment_method_service(db: Session = Depends(get_db)) -> PaymentMethodService:
    repository = PaymentMethodRepository(db)
    return PaymentMethodService(repository)

@router.post("/", response_model=PaymentMethodResponse, status_code=status.HTTP_201_CREATED)
def create_payment_method(payment_method: PaymentMethodCreate,
                          service: PaymentMethodService = Depends(get_payment_method_service)):
    return service.create_payment_method(payment_method)
