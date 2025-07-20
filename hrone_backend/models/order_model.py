from pydantic import BaseModel, Field, validator
from typing import List
from datetime import datetime

class OrderItem(BaseModel):
    productId: str
    qty: int = Field(..., gt=0, description="Quantity must be greater than 0")

class OrderIn(BaseModel):
    userId: str
    items: List[OrderItem]

class OrderOut(BaseModel):
    id: str
    userId: str
    items: List[OrderItem]
    createdAt: datetime
