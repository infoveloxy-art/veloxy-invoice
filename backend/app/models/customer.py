from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    company = Column(String(255), nullable=False)

    address = Column(String(255))

    ico = Column(String(20))

    dic = Column(String(30))

    email = Column(String(255))

    invoices = relationship(
        "Invoice",
        back_populates="customer"
    )
