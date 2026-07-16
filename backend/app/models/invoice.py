from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Boolean,
    Date,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)

    invoice_number = Column(
        String(20),
        unique=True,
        nullable=False
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False
    )

    vehicle_id = Column(
        Integer,
        ForeignKey("vehicles.id"),
        nullable=False
    )

    issue_date = Column(Date)

    due_date = Column(Date)

    subtotal = Column(Float)

    vat_rate = Column(Float)

    vat_amount = Column(Float)

    total = Column(Float)

    use_vat = Column(Boolean)

    note = Column(String(500))

    paid = Column(Boolean, default=False)

    created_at = Column(Date)

updated_at = Column(Date)

    customer = relationship(
        "Customer",
        back_populates="invoices"
    )

    vehicle = relationship(
        "Vehicle",
        back_populates="invoices"
    )
