from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="VELOXY Invoice API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "application": "VELOXY Invoice",
        "company": "Veloxy Trade s.r.o.",
        "status": "Running"
    }
