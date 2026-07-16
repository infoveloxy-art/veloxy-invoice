from fastapi import APIRouter

router = APIRouter()


@router.get("/company")
def get_company():
    return {
        "name": "Veloxy Trade s.r.o.",
        "ico": "19899645",
        "dic": "CZ19899645"
    }
