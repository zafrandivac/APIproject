from .. import schemas, database, models, hashing, oauth2
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(prefix='/user', tags=['User'])


@router.get('/', response_model=List[schemas.ShowUser])
def get_user(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    user_profile = db.query(models.User).all()
    return user_profile


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(
        email=request.email, username=request.username, hash_password=hashing.Hash.bcrypt(request.hash_password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.put('/{id}', status_code=202)
def user_update(id, request: schemas.User, db: Session = Depends(database.get_db)):
    update_detials = db.query(models.User).filter(models.User.id == id)
    if not update_detials.first():
        raise HTTPException(status_code=404, detail="User not found")

    update_detials.update(request)
    db.commit()
    return {'details': 'User details has been updated'}


@router.delete('/{id}')
def remove_user(id, db: Session = Depends(database.get_db)):
    user_removed = db.query(models.User).filter(models.User.id == id)
    if not user_removed.first():
        raise HTTPException(status_code=404, detail="User not found")

    user_removed.delete(synchronize_session=False)
    db.commit()
    return {'details': 'User has been removed'}


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show_user(id, db: Session = Depends(database.get_db)):
    show_profile = db.query(models.User).filter(models.User.id == id).first()
    if not show_profile:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return show_profile
