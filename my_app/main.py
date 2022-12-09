from typing import List
from fastapi import FastAPI, Depends, status, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/login', status_code=status.HTTP_201_CREATED)
def login(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(email=request.email, username=request.username,
                           hash_password=request.hash_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/login', response_model=List[schemas.ShowUser])
def get_user(db: Session = Depends(get_db)):
    user_profile = db.query(models.User).all()
    return user_profile


@app.put('/login/{id}', status_code=202)
def user_update(id, request: schemas.User, db: Session = Depends(get_db)):
    update_detials = db.query(models.User).filter(models.User.id == id)
    if not update_detials.first():
        raise HTTPException(status_code=404, detail="User not found")

    update_detials.update(request)
    db.commit()
    return {'details': 'User details has been updated'}


@app.delete('/login/{id}')
def remove_user(id, db: Session = Depends(get_db)):
    user_removed = db.query(models.User).filter(models.User.id == id)
    if not user_removed.first():
        raise HTTPException(status_code=404, detail="User not found")

    user_removed.delete(synchronize_session=False)
    db.commit()
    return {'details': 'User has been removed'}


@app.get('/login/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show_user(id, db: Session = Depends(get_db)):
    show_profile = db.query(models.User).filter(models.User.id == id).first()
    if not show_profile:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return show_profile
