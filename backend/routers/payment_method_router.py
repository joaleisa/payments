from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from backend.database.database import get_db
from backend.models.payment_method import Payment_Method
from backend.schemas.payment_method_schema import PaymentMethodResponse, PaymentMethodCreate

router = APIRouter(
    prefix="/payment_method",
    tags=["payment_method"]
)

@router.post("/", response_model=PaymentMethodResponse, status_code=status.HTTP_201_CREATED)
def create_payment_method(payment_method: PaymentMethodCreate, db: Session = Depends(get_db)):
    payment_method_exists = db.query(Payment_Method).filter(Payment_Method.name == payment_method.name).first()
    if payment_method_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El metodo de pago ya existe")

    db_payment_method = Payment_Method(**payment_method.dict())
    db.add(db_payment_method)
    db.commit()
    db.refresh(db_payment_method)
    return db_payment_method
