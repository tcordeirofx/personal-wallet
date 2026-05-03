from decimal import Decimal
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, PlainSerializer

_JsonDecimal = Annotated[Decimal, PlainSerializer(float, return_type=float, when_used='json')]


class WalletPositionResponse(BaseModel):
    asset_id: UUID
    symbol: str
    name: str
    asset_type: str
    currency: str
    total_quantity: _JsonDecimal
    average_price: _JsonDecimal
    last_unit_price: _JsonDecimal
    invested_amount: _JsonDecimal
    current_amount: _JsonDecimal
    profit_loss: _JsonDecimal
    profit_loss_percentage: _JsonDecimal


class WalletAllocationResponse(BaseModel):
    asset_type: str
    current_amount: _JsonDecimal
    percentage: _JsonDecimal


class WalletSummaryResponse(BaseModel):
    total_assets: int
    total_quantity: _JsonDecimal
    total_invested: _JsonDecimal
    total_current: _JsonDecimal
    total_profit_loss: _JsonDecimal
    total_profit_loss_percentage: _JsonDecimal
    allocation_by_asset_type: list[WalletAllocationResponse]
