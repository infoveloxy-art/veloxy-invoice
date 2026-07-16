from sqlalchemy import Column, Integer, String

from app.database import Base


class NumberSequence(Base):
    __tablename__ = "number_sequence"

    id = Column(Integer, primary_key=True)

    prefix = Column(String(10), default="2026")

    next_number = Column(Integer, default=1)

    digits = Column(Integer, default=4)
