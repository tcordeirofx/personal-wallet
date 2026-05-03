from datetime import datetime
from decimal import Decimal
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, Field, PlainSerializer

_JsonDecimal = Annotated[Decimal, PlainSerializer(float, return_type=float, when_used='json')]


class WalletEntryCreate(BaseModel):
    asset_id: UUID
    quantity: _JsonDecimal = Field(gt=0)
    unit_price: _JsonDecimal = Field(gt=0)


class WalletEntry(WalletEntryCreate):
    id: UUID
    created_at: datetime
