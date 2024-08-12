from pydantic import BaseModel
from src.seller.schemas import DisplaySeller

class Product(BaseModel):
    name : str
    description: str
    price: int

class DisplayProduct(BaseModel):
    name: str
    description: str
    seller: DisplaySeller

    class Config:
        from_attributes = True


