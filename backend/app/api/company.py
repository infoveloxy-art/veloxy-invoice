from fastapi import APIRouter

from app.services.company_service import CompanyService

router = APIRouter(prefix="/company", tags=["Company"])


@router.get("")
def get_company():
    return CompanyService.get_company()
