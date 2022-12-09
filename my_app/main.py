from fastapi import FastAPI
from . import models
from .database import engine
from .routers import item, user, autentication

app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(autentication.router)
app.include_router(user.router)
app.include_router(item.router)
