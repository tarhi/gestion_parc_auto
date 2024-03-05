from app.projet import app
from app.projet.models_auth import PostSchema, userSchema, loginuserSchema
from app.projet.jwt_handler import signJWT
from app.projet.jwt_bearer import JWTbearer
from fastapi import Depends



users = []

def cheek_user(data:loginuserSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        else:
            False

@app.post("/user/signup", tags= ["user"])
def create_user(user:userSchema):
    users.append(user)
    return signJWT(user.email)



@app.post("/user/login", tags= ["user"])
def user_login(user:loginuserSchema):
    if cheek_user(user):
        return signJWT(user.email)
    return {"Wrong login !!!"}





