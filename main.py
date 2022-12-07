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

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": {"name": "Zafran"}}
