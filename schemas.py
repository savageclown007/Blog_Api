from pydantic import BaseModel
from typing import List, Optional, Union

class Blog(BaseModel):
    title: str
    body: str

class Blogs(Blog):
    title: str
    body: str

    class Config:
        orm_mode=True


class User(BaseModel):
    name:str
    email:str
    password:str
    
class Users(BaseModel):
    name:str
    email:str
    class Config:
        orm_mode=True

class ShowUser(BaseModel):
    name:str
    email:str
    blogs: List[Blogs]
    class Config:
        orm_mode=True

class ShowBlog(Blog):
    creator: Users
    class Config:
        orm_mode=True

class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
