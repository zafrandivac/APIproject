from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, models, database, hashing, ilovetoken
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/login', tags=["User Login"])
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not hashing.Hash.verify(user.hash_password, request.password):
        raise HTTPException(status_code=404, detail="Incorrect Password")

    access_token = ilovetoken.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
