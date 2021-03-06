import os, shutil
from starlette.requests import Request
from fastapi import APIRouter, HTTPException, Depends

from app.auth.auth_bearer import JwtBearer

from app.models.inventory import InventPydantic, Inventory
from app.models.utils import Status


from tortoise.contrib.fastapi import HTTPNotFoundError

BASE_PATH = os.path.abspath(os.curdir)
STATIC_DIR = os.path.join(BASE_PATH, 'app/static')


async def save_file(picture):
    with open(f'{STATIC_DIR}/images/{picture.filename}', 'wb') as buffer:
        try:
            shutil.copyfileobj(picture.file, buffer)
        except Exception as e:
            print(e)
        else:
            return True


router = APIRouter()


@router.get("/", dependencies=[Depends(JwtBearer())])
async def all_inventory():
    return await InventPydantic.from_queryset(Inventory.all().order_by('-id'))


@router.get("/item/{item_id}", response_model=InventPydantic)
async def get_by_id(item_id: int):
    return await InventPydantic.from_queryset_single(Inventory.get(id=item_id))


@router.post('/item')
async def create_inventory(request: Request):
    form_data = await request.form()
    inventory_obj = await Inventory(
        name=form_data.get('name'),
        image_name=form_data.get('image_name'),
        price=form_data.get('price'),
        stock=form_data.get('stock')
    )
    await inventory_obj.save()
    await save_file(form_data.get('picture'))
    return await InventPydantic.from_tortoise_orm(inventory_obj)


async def check_image_exist(picture):
    if type(picture) is str:
        return False
    else:
        return True


@router.put("/item/{item_id}")
async def update_inventory(item_id: int, request: Request):
    if await Inventory.filter(id=item_id).exists():
        form_data = await request.form()
        is_has_picture = await check_image_exist(form_data.get('picture'))
        if is_has_picture:
            await Inventory.filter(id=item_id).update(
                name=form_data.get('name'),
                price=form_data.get('price'),
                stock=form_data.get('stock'),
                image_name=form_data.get('image_name')
            )
            await save_file(form_data.get('picture'))
        else:
            await Inventory.filter(id=item_id).update(
                name=form_data.get('name'),
                price=form_data.get('price'),
                stock=form_data.get('stock'),
            )
        return await InventPydantic.from_queryset_single(Inventory.get(id=item_id))
    else:
        raise HTTPException(status_code=404, detail=f'Id {item_id} not found')


@router.delete(
    "/item/{id}",
    response_model=Status,
    responses={404: {'model': HTTPNotFoundError}}
)
async def delete_inventory(id: int):
    delete_count = await Inventory.filter(id=id).delete()
    if not delete_count:
        raise HTTPException(status_code=404, detail=f'Item {id} not found')
    return Status(message=f'Delete item {id}')
