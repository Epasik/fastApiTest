from pydantic import BaseModel
from typing import Optional

# Схемы для валидации данных (через Pydantic)
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True  # Позволяет работать с ORM