import os, shutil
from fastapi import APIRouter, UploadFile, File, Form
from models.inventory import InventPydantic, InventPydanticIn, Inventory

BASE_PATH = os.path.abspath(os.curdir)
STATIC_DIR = os.path.join(BASE_PATH, 'static')

async def save_file(image_name):
    with open(f'{STATIC_DIR}/images/{image_name.filename}', 'wb') as buffer:
        try:
            shutil.copyfileobj(image_name.file, buffer)
        except Exception as e:
            print(e)
        else:
            return True

router = APIRouter()


@router.get("/")
async def all_inventory():
    return await InventPydantic.from_queryset(Inventory.all())


@router.get("/item/{id}")
async def get_by_id(id: int):
    return { 'id': id }


@router.post('/item')
async def create_inventory(
    name: str = Form(...),
    price: float = Form(...),
    stock: int = Form(...),
    image_name: UploadFile = File(...)
):

    Inventory_obj = await Inventory(
        name=name,
        image_name=image_name.filename,
        price=price,
        stock=stock
    )
    await Inventory_obj.save()
    await save_file(image_name)
    return await InventPydantic.from_tortoise_orm(Inventory_obj)


@router.put("/item/{id}")
async def update_inventory(id: int):
    return { 'id': id }


@router.delete("/item/{id}")
async def delete_inventory(id: int):
    return { 'id': id }

