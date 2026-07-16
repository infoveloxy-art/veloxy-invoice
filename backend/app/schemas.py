from pydantic import BaseModel
from typing import Optional


class CompanyBase(BaseModel):
    name: str
    address: str
    ico: str
    dic: str
    iban: str
    swift: str
    email: str
    bank: str


class CompanyCreate(CompanyBase):
    pass


class CompanyResponse(CompanyBase):
    id: int

    class Config:
        from_attributes = True
        from datetime import date


class InvoiceCreate(BaseModel):
    customer_id: int
    vehicle_id: int

    issue_date: date
    due_date: date

    amount: float

    use_vat: bool = True

    note: Optional[str] = None


class InvoiceResponse(BaseModel):
    id: int

    invoice_number: str

    subtotal: float

    vat_rate: float

    vat_amount: float

    total: float

    use_vat: bool

    paid: bool

    class Config:
        from_attributes = True
