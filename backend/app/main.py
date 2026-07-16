from fastapi import FastAPI

app = FastAPI(
    title="VELOXY Invoice API",
    version="1.0.0",
    description="Backend для системы выставления фактур VELOXY"
)


@app.get("/")
def root():
    return {
        "company": "VELOXY Trade s.r.o.",
        "application": "VELOXY Invoice",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }
