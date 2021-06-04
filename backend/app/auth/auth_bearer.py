from fastapi import Request, HTTPException, status
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.security.base import SecurityBase

from .auth_handler import decode_jwt

def verify_jwt(jwt_token: str) -> bool:
    is_token_valid: bool = False
    try:
        payload = decode_jwt(jwt_token)
    except:
        payload = None
    if payload:
        is_token_valid = True
    return is_token_valid


class JwtBearer(SecurityBase):
    def __init__(self, scheme_name: str = None, auto_error: bool = True):
        self.scheme_name = scheme_name or self.__class__.__name__
        self.auto_error = auto_error

    async def __call__(self, request: Request):
        authorization: str = request.headers.get('Authorization')
        if authorization:
            scheme, token = get_authorization_scheme_param(authorization)
            if scheme == 'Bearer':
                if verify_jwt(token) is False:
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail='Invalid token or expire token.'
                    )
                return token
            else:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail='Invalid authorization code.'
                )
