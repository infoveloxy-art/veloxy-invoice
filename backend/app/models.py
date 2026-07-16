from sqlalchemy import Column, Integer, String

from .database import Base


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    address = Column(String)

    ico = Column(String)

    dic = Column(String)

    iban = Column(String)

    swift = Column(String)

    email = Column(String)

    bank = Column(String)

    logo = Column(String)
