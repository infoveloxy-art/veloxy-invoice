from fastapi import APIRouter

from .company import router as company_router
from .customer import router as customer_router
from .vehicle import router as vehicle_router
from .invoice import router as invoice_router

router = APIRouter()

router.include_router(company_router)
router.include_router(customer_router)
router.include_router(vehicle_router)
router.include_router(invoice_router)
