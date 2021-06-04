import time
from typing import Dict

import jwt
from decouple import config


JWT_SECRET = config('secret')
JWT_ALGORITHM = config('algorithm')


def token_response(username: str, token: str):
    return {
        'username': username,
        'access_token': token
    }


def sign_jwt(username: str) -> Dict[str, str]:
    payload = {
        'user_name': username,
        'expire': time.time() + 600,
    }
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token_response(username, token)


def decode_jwt(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        return decode_token if decode_token.get('expire') >= time.time() else None
    except:
        return {}

