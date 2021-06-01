import sys
from fastapi import APIRouter
sys.path.append('..')
from models.user import UserPydantic, UserInPydantic, User
from passlib.hash import bcrypt

router = APIRouter()


@router.post('/token')


@router.get("/")
async def show_all_user():
    return await UserPydantic.from_queryset(User.all().order_by('-id'))


@router.post('/create_user', response_model=UserPydantic)
async def create_user(user: UserInPydantic):
    user_obj = await User(
        username=user.username,
        password_hash=bcrypt.hash(user.password_hash)
    )

    await user_obj.save()
    return await UserPydantic.from_tortoise_orm(user_obj)
