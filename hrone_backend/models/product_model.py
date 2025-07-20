from pydantic import BaseModel, Field
from typing import List

class Size(BaseModel):
    size: str
    quantity: int

class ProductIn(BaseModel):
    name: str
    price: float
    sizes: List[Size]

class ProductOut(BaseModel):
    id: str
    name: str
    price: float
