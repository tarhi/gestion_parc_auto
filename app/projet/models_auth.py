from pydantic import BaseModel, EmailStr, Field



class PostSchema(BaseModel):
    __tablename__="posteSchema"
    id: int = Field(default=None)
    title: str = Field(default=None)
    Content:  str = Field(default=None)

class userSchema(BaseModel):
    __tablename__="userSchema"
    fullname : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)

class loginuserSchema(BaseModel):
    __tablename__="login"
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)


