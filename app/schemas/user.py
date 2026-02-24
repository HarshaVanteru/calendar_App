
from pydantic import BaseModel, EmailStr,Field

class UserRegister(BaseModel):
    email:EmailStr
    password:str = Field(min_length=3)

class UserLogin(BaseModel):
    email:EmailStr
    password:str = Field(min_length=3)

class Token(BaseModel):
    access_token:str
    token_type:str