from fastapi import APIRouter
from .inventorys import router as inventory_router


router = APIRouter()

router.include_router(inventory_router, prefix="/inventory", tags=["inventory"])
