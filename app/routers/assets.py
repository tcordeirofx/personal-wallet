from fastapi import APIRouter

from app.schemas.asset import Asset, AssetCreate
from app.services.asset_service import AssetService

router = APIRouter(prefix="/assets", tags=["assets"])

_service = AssetService()


@router.get("/", response_model=list[Asset])
def list_assets() -> list[Asset]:
    return _service.list_all()


@router.post("/", status_code=201, response_model=Asset)
def create_asset(data: AssetCreate) -> Asset:
    return _service.create(data)
