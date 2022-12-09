from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    username: str
    hash_password: str


class ShowUser(BaseModel):
    email: str
    username: str

    class Config():
        orm_mode = True
