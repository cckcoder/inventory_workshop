from app.models.user import UserPydantic, UserInPydantic, User
from app.auth.auth_bearer import JwtBearer
from app.auth.auth_handler import sign_jwt

from fastapi import APIRouter, Depends, HTTPException, status, Depends, Request


router = APIRouter()


async def authenticate_user(username: str, password: str):
    user = await User.get(username=username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )

    if not user.vefify_password(password=password):
        return False
    else:
        return user


@router.get("/")
async def show_all_user():
    return await UserPydantic.from_queryset(User.all().order_by('-id'))


@router.post('/login')
async def generate_token(request: Request):
    form_data = await request.form()
    user = await authenticate_user(
        form_data.get('username'),
        form_data.get('password')
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )

    return sign_jwt(user.username)



@router.post('/register', response_model=UserPydantic)
async def create_user(user: UserInPydantic):
    user_obj = await User(
        username=user.username,
        password_hash= User.get_password_hash(user.password_hash)
    )

    await user_obj.save()
    return await UserPydantic.from_tortoise_orm(user_obj)
