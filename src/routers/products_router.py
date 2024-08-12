from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..product import models
from ..product import schemas
from ..database import engine, get_db
from src.seller.schemas import Seller
from src.routers.login_router import get_current_user
from typing import List

router = APIRouter(
    prefix="/products"
)

models.Base.metadata.create_all(engine)


@router.get('', response_model=List[schemas.DisplayProduct])
async def product_list(db:Session=Depends(get_db), current_user: Seller = Depends(get_current_user)):
    products = db.query(models.Product).all()
    return products

@router.get('/{id}', response_model=schemas.DisplayProduct)
def get_product(id, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with ID {id} not found")
    return product

@router.post('', status_code=status.HTTP_201_CREATED)
async def add(request: schemas.Product, db: Session= Depends(get_db)):
    new_product = models.Product(name=request.name, description=request.description,price=request.price, seller_id=1)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request

@router.put('/{id}')
async def update(id, request: schemas.Product, db:Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with ID {id} not found")
    product.update(request.dict())
    db.commit()
    return {'updated'}
    

