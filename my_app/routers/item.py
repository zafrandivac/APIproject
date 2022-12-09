from .. import schemas, database, models, hashing
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(prefix='/item', tags=['Item'])


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowItem)
def create_item(request: schemas.Item, db: Session = Depends(database.get_db)):
    new_item = models.Item(name=request.item_name, price=request.item_price)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.get('/', response_model=List[schemas.ShowItem])
def get_item(db: Session = Depends(database.get_db)):
    item_details = db.query(models.Item).all()
    return item_details


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowItem)
def show_specific_item(id, db: Session = Depends(database.get_db)):
    show_item = db.query(models.Item).filter(models.Item.id == id).first()
    if not show_item:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return show_item
