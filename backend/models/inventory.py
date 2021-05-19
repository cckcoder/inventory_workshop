from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Inventory(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(100)
    image_name = fields.TextField()
    price = fields.DecimalField(max_digits=10, decimal_places=3)
    stock = fields.IntField()
    created_date = fields.DateField(auto_now_add=True)
    updated_date = fields.DateField(auto_now=True)
