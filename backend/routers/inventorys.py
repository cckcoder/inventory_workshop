from fastapi import APIRouter

router = APIRouter()


@router.get("/inventory", tags=['inventory'])
async def all_inventory():
    return {'inventory': 'Okay'}
