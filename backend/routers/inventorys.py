from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def all_inventory():
    return {'inventory': 'Okay'}


@router.get("/item/{id}")
async def get_by_id(id: int):
    return { 'id': id }


@router.put("/item/{id}")
async def update_inventory(id: int):
    return { 'id': id }


@router.delete("/item/{id}")
async def delete_inventory(id: int):
    return { 'id': id }

