from fastapi import APIRouter
from .inventorys import router as inventory_router
from .users import router as user_router


router = APIRouter()

router.include_router(inventory_router, prefix="/inventory", tags=["inventory"])
router.include_router(user_router, prefix="/user", tags=["user"])
