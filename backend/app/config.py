from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "VELOXY Invoice"
    VERSION: str = "1.0.0"

    COMPANY_NAME: str = "Veloxy Trade s.r.o."
    COMPANY_ADDRESS: str = "Uralská 689/7, 160 00 Praha 6"

    ICO: str = "19899645"
    DIC: str = "CZ19899645"

    EMAIL: str = "info@veloxy.cz"

    BANK: str = "Česká spořitelna"

    IBAN: str = "CZ0408000000006610568389"

    SWIFT: str = "GIBACZPX"


settings = Settings()
