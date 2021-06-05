from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password):
    return pwd_context.hash(password)


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    password_hash = fields.CharField(150)

    def vefify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


UserPydantic = pydantic_model_creator(User, name='User')
UserInPydantic = pydantic_model_creator(
    User, name='UserIn', exclude_readonly=True
)
