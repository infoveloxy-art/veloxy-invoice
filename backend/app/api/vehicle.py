from fastapi import APIRouter

router = APIRouter(
    prefix="/vehicle",
    tags=["Vehicle"]
)


@router.get("/")
def get_vehicles():
    return {
        "items": []
    }
