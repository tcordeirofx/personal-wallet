from uuid import UUID
from pydantic import BaseModel


class AssetPosition(BaseModel):
    asset_id: UUID
    symbol: str
    name: str
    asset_type: str
    currency: str
    total_quantity: float
    average_price: float
    last_unit_price: float
    invested_amount: float
    current_amount: float
    profit_loss: float
    profit_loss_percentage: float
