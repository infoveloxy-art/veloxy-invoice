from app.config import settings


class CompanyService:

    @staticmethod
    def get_company():

        return {

            "name": settings.COMPANY_NAME,

            "address": settings.COMPANY_ADDRESS,

            "ico": settings.ICO,

            "dic": settings.DIC,

            "email": settings.EMAIL,

            "bank": settings.BANK,

            "iban": settings.IBAN,

            "swift": settings.SWIFT

        }
