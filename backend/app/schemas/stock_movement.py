from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class StockMovementBase(BaseModel):
    product_id: int
    type: str  # 'ENTRY', 'EXIT', 'SALE', 'RETURN', 'ADJUSTMENT'
    quantity: int
    reason: Optional[str] = None
    reference_type: Optional[str] = None
    reference_id: Optional[int] = None

class StockMovementCreate(StockMovementBase):
    pass

class StockMovement(StockMovementBase):
    id: int
    user_id: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True
