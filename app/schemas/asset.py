from uuid import UUID
from pydantic import BaseModel, Field


class AssetCreate(BaseModel):
    symbol: str = Field(min_length=1)
    name: str = Field(min_length=1)
    asset_type: str = Field(min_length=1)
    currency: str = Field(min_length=1)


class AssetUpdate(BaseModel):
    symbol: str | None = Field(default=None, min_length=1)
    name: str | None = Field(default=None, min_length=1)
    asset_type: str | None = Field(default=None, min_length=1)
    currency: str | None = Field(default=None, min_length=1)


class Asset(AssetCreate):
    id: UUID
