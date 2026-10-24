from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    price: Decimal = Field(ge=0, max_digits=12, decimal_places=2)
    stock_quantity: int = Field(default=0, ge=0)


class ProductResponse(BaseModel):
    id: int
    name: str
    price: Decimal
    stock_quantity: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)