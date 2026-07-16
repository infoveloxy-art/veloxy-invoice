from sqlalchemy import Column, Integer, Float, String, Boolean, Date

from app.database import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)

    invoice_number = Column(String(50), unique=True)

    customer_id = Column(Integer)

    vehicle_id = Column(Integer)

    issue_date = Column(Date)

    due_date = Column(Date)

    total = Column(Float)

    vat = Column(Boolean, default=True)

    paid = Column(Boolean, default=False)
