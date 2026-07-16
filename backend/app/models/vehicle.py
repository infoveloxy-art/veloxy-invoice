from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)

    brand = Column(String(100), nullable=False)

    model = Column(String(100), nullable=False)

    vin = Column(String(100), unique=True)

    price = Column(Float)

    status = Column(
        String(30),
        default="AVAILABLE"
    )

    invoices = relationship(
        "Invoice",
        back_populates="vehicle"
    )
