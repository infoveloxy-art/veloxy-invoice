from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    Date,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.database import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)

    invoice_number = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False,
    )

    vehicle_id = Column(
        Integer,
        ForeignKey("vehicles.id"),
        nullable=False,
    )

    issue_date = Column(Date, nullable=False)

    due_date = Column(Date, nullable=False)

    subtotal = Column(Float, default=0)

    vat_rate = Column(Float, default=21)

    vat_amount = Column(Float, default=0)

    total = Column(Float, default=0)

    use_vat = Column(Boolean, default=True)

    note = Column(String(500), nullable=True)

    paid = Column(Boolean, default=False)

    customer = relationship("Customer")

    vehicle = relationship("Vehicle")
