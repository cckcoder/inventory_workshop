from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel

class InventoryBase(BaseModel):
    name: str
    image_name: str
    price: float
    stock: int

class Inventory(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(100)
    image_name = fields.TextField()
    price = fields.DecimalField(max_digits=10, decimal_places=3)
    stock = fields.IntField()
    created_date = fields.DatetimeField(auto_now_add=True)
    updated_date = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name


InventPydantic = pydantic_model_creator(Inventory, name='Inventory')
InventPydanticIn = pydantic_model_creator(
    Inventory, name='InventoryIn', exclude_readonly=True
)

