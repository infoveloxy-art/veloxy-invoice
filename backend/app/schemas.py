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
