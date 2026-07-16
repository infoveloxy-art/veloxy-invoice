from fastapi import APIRouter

router = APIRouter(
    prefix="/invoice",
    tags=["Invoice"]
)


@router.get("")
def invoices():

    return {
        "items": []
    }
