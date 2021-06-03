import sys
import jwt

sys.path.append('..')
from models.user import UserPydantic, UserInPydantic, User
from passlib.hash import bcrypt

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter()

JWT_SECRET = "myjwtsecret"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

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






async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        user = await User.get(id=payload.get('id'))
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )

    return await UserPydantic.from_tortoise_orm(user)

@router.get("/")
async def show_all_user():
    return await UserPydantic.from_queryset(User.all().order_by('-id'))


@router.post('/token')
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )

    user_obj = await UserPydantic.from_tortoise_orm(user)

    token = jwt.encode(user_obj.dict(), JWT_SECRET)
    return {
        'access_token': token,
        'token_type': 'bearer'
    }


@router.post('/register', response_model=UserPydantic)
async def create_user(user: UserInPydantic):
    user_obj = await User(
        username=user.username,
        password_hash=bcrypt.hash(user.password_hash)
    )

    await user_obj.save()
    return await UserPydantic.from_tortoise_orm(user_obj)

@router.get('/me', response_model=UserPydantic)
async def get_user(user: UserPydantic = Depends(get_current_user)):
    return user

