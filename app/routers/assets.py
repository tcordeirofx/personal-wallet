from uuid import UUID

from fastapi import APIRouter, HTTPException, Response

from app.dependencies import asset_repository, entry_repository
from app.schemas.asset import Asset, AssetCreate, AssetUpdate
from app.services.asset_service import AssetService

router = APIRouter(prefix="/assets", tags=["assets"])

_service = AssetService(repo=asset_repository, entry_repo=entry_repository)


@router.get("/", response_model=list[Asset])
def list_assets() -> list[Asset]:
    return _service.list_all()


@router.post("/", status_code=201, response_model=Asset)
def create_asset(data: AssetCreate) -> Asset:
    try:
        return _service.create(data)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))


@router.put("/{asset_id}/", response_model=Asset)
def update_asset(asset_id: UUID, data: AssetUpdate) -> Asset:
    try:
        asset = _service.update(asset_id, data)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset


@router.delete("/{asset_id}/", status_code=204)
def delete_asset(asset_id: UUID) -> Response:
    try:
        deleted = _service.delete(asset_id)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    if not deleted:
        raise HTTPException(status_code=404, detail="Asset not found")
    return Response(status_code=204)
