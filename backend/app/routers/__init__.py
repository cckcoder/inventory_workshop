from fastapi import APIRouter
from app.routers.inventorys import router as inventory_router
from app.routers.users import router as user_router


router = APIRouter()

router.include_router(inventory_router, prefix="/inventory", tags=["inventory"])
router.include_router(user_router, prefix="/user", tags=["user"])
