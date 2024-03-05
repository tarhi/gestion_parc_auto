from typing_extensions import Annotated, Doc
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from app.projet.jwt_handler import decodeJWT
from .jwt_handler import decodeJWT

class JWTbearer(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super(JWTbearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTbearer,self).__call__(request)
        if credentials:
            if not credentials.scheme == "bearer":
                raise HTTPException(status_code= 403, detail= " Invalid authentification !!!")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail= " Invalid Token")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail= " Invalid authentification code")
    
    def verify_jwt(self, jwtoken: str):
        istokenvalid: bool = False
        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            istokenvalid = True
        return istokenvalid
