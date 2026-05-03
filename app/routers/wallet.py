from fastapi import APIRouter

from app.dependencies import asset_repository, entry_repository
from app.schemas.wallet import AssetPosition, WalletSummary
from app.services.wallet_service import WalletService

router = APIRouter(prefix="/wallet", tags=["wallet"])

_service = WalletService(asset_repo=asset_repository, entry_repo=entry_repository)


@router.get("/positions/", response_model=list[AssetPosition])
def get_positions() -> list[AssetPosition]:
    return _service.get_positions()


@router.get("/summary/", response_model=WalletSummary)
def get_summary() -> WalletSummary:
    return _service.get_summary()
