from fastapi import APIRouter

from app.services.company_service import CompanyService

router = APIRouter()


@router.get("/company")
def company():

    return CompanyService.get_company()
