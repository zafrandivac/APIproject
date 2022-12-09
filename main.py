# import uvicorn
# import models
# import schemas

# from routers import user, authentication
# from fastapi import FastAPI, Depends
# from basisdata import engine, SessionLocal, get_basisdata
# from sqlalchemy.orm import Session

# app = FastAPI()

# models.Base.metadata.create_all(bind=engine)

# app.include_router(user.router)
# app.include_router(authentication.router)


# def migrate_table():
#     return


# if __name__ == '__main__':
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

from typing import Union, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    password: str
    access_granted: Optional[bool]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/login")
def user_login(user: User):
    return {'text': f'Login Successfully, Welcome Back {user.username}'}
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}
