from sqlalchemy import Column, Integer, String, Float

from app.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True)

    brand = Column(String(100))

    model = Column(String(100))

    vin = Column(String(100), unique=True)

    price = Column(Float)

    status = Column(String(30), default="AVAILABLE")
