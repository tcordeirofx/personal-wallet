from fastapi import APIRouter, HTTPException

from app.dependencies import asset_repository, entry_repository
from app.schemas.entry import WalletEntry, WalletEntryCreate
from app.services.entry_service import EntryService

router = APIRouter(prefix="/entries", tags=["entries"])

_service = EntryService(asset_repo=asset_repository, entry_repo=entry_repository)


@router.get("/", response_model=list[WalletEntry])
def list_entries() -> list[WalletEntry]:
    return _service.list_all()


@router.post("/", status_code=201, response_model=WalletEntry)
def create_entry(data: WalletEntryCreate) -> WalletEntry:
    try:
        return _service.create(data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
