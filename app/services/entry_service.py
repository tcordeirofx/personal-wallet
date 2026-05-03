from app.repositories.memory_repository import AssetRepository, EntryRepository
from app.schemas.entry import WalletEntry, WalletEntryCreate


class EntryService:
    def __init__(self, asset_repo: AssetRepository, entry_repo: EntryRepository) -> None:
        self._asset_repo = asset_repo
        self._entry_repo = entry_repo

    def create(self, data: WalletEntryCreate) -> WalletEntry:
        if self._asset_repo.get_by_id(data.asset_id) is None:
            raise ValueError(f"Asset '{data.asset_id}' not found")
        return self._entry_repo.create(data)
