from fastapi import FastAPI

from app.api.router import router
from app.config import settings
from app.init_db import create_database

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)


@app.on_event("startup")
def startup():
    create_database()


app.include_router(router)


@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.VERSION,
        "status": "Running"
    }
