from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    email: str
    username: str
    hash_password: str


class Item(BaseModel):
    item_name: str
    item_price: int


class ShowUser(BaseModel):
    email: str
    username: str

    class Config():
        orm_mode = True


class ShowItem(BaseModel):
    item_name: str
    item_price: int

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
