from fastapi import APIRouter

from app.dependencies import asset_repository, entry_repository
from app.schemas.wallet import WalletPositionResponse, WalletSummaryResponse
from app.services.wallet_service import WalletService

router = APIRouter(prefix="/wallet", tags=["wallet"])

_service = WalletService(asset_repo=asset_repository, entry_repo=entry_repository)


@router.get("/positions/", response_model=list[WalletPositionResponse])
def get_positions() -> list[WalletPositionResponse]:
    return _service.get_positions()


@router.get("/summary/", response_model=WalletSummaryResponse)
def get_summary() -> WalletSummaryResponse:
    return _service.get_summary()
