from fastapi import APIRouter
from models.inventory import InventPydantic, InventPydanticIn, Inventory

router = APIRouter()


@router.get("/")
async def all_inventory():
    return await InventPydantic.from_queryset(Inventory.all())


@router.get("/item/{id}")
async def get_by_id(id: int):
    return { 'id': id }


@router.post('/item', response_model=InventPydantic)
async def create_inventory(inventory: InventPydanticIn):
    inventory_obj = await Inventory.create(**inventory.dict(exclude_unset=True))
    return await InventPydantic.from_tortoise_orm(inventory_obj)


@router.put("/item/{id}")
async def update_inventory(id: int):
    return { 'id': id }


@router.delete("/item/{id}")
async def delete_inventory(id: int):
    return { 'id': id }

