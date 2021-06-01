from fastapi import APIRouter
from models.user import UserPydantic, UserInPydantic, User

router = APIRouter()


@router.get("/")
async def show_all_user():
    return await UserPydantic.from_queryset(User.all().order_by('-id'))  
