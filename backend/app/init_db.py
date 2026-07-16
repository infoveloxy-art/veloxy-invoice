from app.database import Base, engine

# Импортируем все модели, чтобы SQLAlchemy зарегистрировала таблицы
from app.models.company import Company
from app.models.customer import Customer
from app.models.vehicle import Vehicle
from app.models.invoice import Invoice
from app.models.sequence import NumberSequence


def create_database():
    Base.metadata.create_all(bind=engine)
