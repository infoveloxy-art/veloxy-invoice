from sqlalchemy import Column, Integer, String

from app.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)

    company = Column(String(255))

    address = Column(String(255))

    ico = Column(String(20))

    dic = Column(String(30))

    email = Column(String(255))
