from uuid import UUID
from pydantic import BaseModel, Field, field_validator


class AssetCreate(BaseModel):
    symbol: str = Field(min_length=1)
    name: str = Field(min_length=1)
    asset_type: str = Field(min_length=1)
    currency: str = Field(min_length=1)

    @field_validator("symbol", "currency", mode="before")
    @classmethod
    def to_uppercase(cls, v: str) -> str:
        return v.upper()


class AssetUpdate(BaseModel):
    symbol: str | None = Field(default=None, min_length=1)
    name: str | None = Field(default=None, min_length=1)
    asset_type: str | None = Field(default=None, min_length=1)
    currency: str | None = Field(default=None, min_length=1)

    @field_validator("symbol", "currency", mode="before")
    @classmethod
    def to_uppercase(cls, v: str | None) -> str | None:
        return v.upper() if v is not None else None


class Asset(AssetCreate):
    id: UUID
