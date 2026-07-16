from sqlalchemy import Column, Integer, String

from app.database import Base


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)

    name = Column(String(255))

    address = Column(String(255))

    ico = Column(String(20))

    dic = Column(String(30))

    email = Column(String(255))

    bank = Column(String(255))

    iban = Column(String(100))

    swift = Column(String(20))

    logo = Column(String(255))
