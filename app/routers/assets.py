from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.schemas.asset import Asset, AssetCreate, AssetUpdate
from app.services.asset_service import AssetService

router = APIRouter(prefix="/assets", tags=["assets"])

_service = AssetService()


@router.get("/", response_model=list[Asset])
def list_assets() -> list[Asset]:
    return _service.list_all()


@router.post("/", status_code=201, response_model=Asset)
def create_asset(data: AssetCreate) -> Asset:
    return _service.create(data)


@router.put("/{asset_id}/", response_model=Asset)
def update_asset(asset_id: UUID, data: AssetUpdate) -> Asset:
    asset = _service.update(asset_id, data)
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset
