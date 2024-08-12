from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ..database import Base

class Seller(Base):
    __tablename__='seller'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    products = relationship('Product', back_populates='seller')