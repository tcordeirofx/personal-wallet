from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field


class WalletEntryCreate(BaseModel):
    asset_id: UUID
    quantity: float = Field(gt=0)
    unit_price: float = Field(gt=0)


class WalletEntry(WalletEntryCreate):
    id: UUID
    created_at: datetime
