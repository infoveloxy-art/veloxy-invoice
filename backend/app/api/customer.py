from fastapi import APIRouter

router = APIRouter(
    prefix="/customer",
    tags=["Customer"]
)


@router.get("")
def customers():

    return {
        "items": []
    }
