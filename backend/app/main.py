from fastapi import FastAPI

from app.api import router

from app.config import settings

app = FastAPI(

    title=settings.APP_NAME,

    version=settings.VERSION

)

app.include_router(router)


@app.get("/")
def root():

    return {

        "application": settings.APP_NAME,

        "version": settings.VERSION,

        "status": "Running"

    }
