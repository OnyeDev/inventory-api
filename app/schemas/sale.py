from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class SaleCreate(BaseModel):
    user_id: int = Field(gt=0)


class SaleResponse(BaseModel):
    id: int
    user_id: int
    total_amount: Decimal
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)