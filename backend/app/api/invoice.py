from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import InvoiceCreate
from app.services.invoice_service import InvoiceService

router = APIRouter(
    prefix="/invoice",
    tags=["Invoice"]
)


@router.post("/")
def create_invoice(
    data: InvoiceCreate,
    db: Session = Depends(get_db),
):
    return InvoiceService.create_invoice(db, data)
