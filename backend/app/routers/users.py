from app.models.user import UserPydantic,  User, get_password_hash
from app.auth.auth_handler import sign_jwt

from fastapi import APIRouter,  HTTPException, status, Request

router = APIRouter()


async def authenticate_user(username: str, password: str):
    user = await User.get_or_none(username=username)
    if user is None:
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


@router.post('/register')
async def create_user(request: Request):
    form_data = await request.form()
    username = form_data.get('username')
    is_exist = await User.filter(username=username).count()

    if is_exist:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Duplicate username'
        )

    user_obj = await User(
        username=form_data.get('username'),
        password_hash=get_password_hash(form_data.get('password'))
    )

    await user_obj.save()
    return sign_jwt(form_data.get('username'))
