from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from . import models
from . import schemas
from .database import engine, SessionLocal
from typing import List


router = APIRouter()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/products', response_model=List[schemas.DisplayProduct])
async def product_list(db:Session=Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@router.get('/products/{id}', response_model=schemas.DisplayProduct)
def get_product(id, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with ID {id} not found")
    return product

@router.post('/products', status_code=status.HTTP_201_CREATED)
async def add(request: schemas.Product, db: Session= Depends(get_db)):
    new_product = models.Product(name=request.name, description=request.description,price=request.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request

@router.put('/products/{id}')
async def update(id, request: schemas.Product, db:Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with ID {id} not found")
    product.update(request.dict())
    db.commit()
    return {'updated'}
    

