import time
from typing import Dict
from jose import jwt

jwt_secret = "c1c83e4de90ecc475a1ef08d0c652a80"
algorithm = "HS256"

def token_response(token: str):
    return {"token": token}

# function used for signin JWT

def signJWT(user_ID: str):
    payload = {
        "user_ID" : user_ID,
        "expire" : time.time() + 600
    }
    token = jwt.encode(payload, jwt_secret, algorithm=algorithm)
    return token_response(token)

def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token,jwt_secret,algorithms=[algorithm])
        return decode_token if decode_token["expire"] >= time.time() else None
    except:
        return{}
