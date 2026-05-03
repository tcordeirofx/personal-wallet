from uuid import UUID

from app.repositories.memory_repository import AssetRepository, EntryRepository
from app.schemas.asset import Asset, AssetCreate, AssetUpdate


class AssetService:
    def __init__(
        self,
        repo: AssetRepository | None = None,
        entry_repo: EntryRepository | None = None,
    ) -> None:
        self._repo = repo if repo is not None else AssetRepository()
        self._entry_repo = entry_repo

    def create(self, data: AssetCreate) -> Asset:
        if self._repo.get_by_symbol(data.symbol) is not None:
            raise ValueError(f"Asset with symbol '{data.symbol}' already exists")
        return self._repo.create(data)

    def list_all(self) -> list[Asset]:
        return self._repo.list_all()

    def update(self, asset_id: UUID, data: AssetUpdate) -> Asset | None:
        if data.symbol is not None:
            existing = self._repo.get_by_symbol(data.symbol)
            if existing is not None and existing.id != asset_id:
                raise ValueError(f"Asset with symbol '{data.symbol}' already exists")
        return self._repo.update(asset_id, data)

    def delete(self, asset_id: UUID) -> bool:
        if self._entry_repo is not None:
            entries = self._entry_repo.list_by_asset(asset_id)
            if entries:
                raise ValueError(f"Asset '{asset_id}' has {len(entries)} associated entries")
        return self._repo.delete(asset_id)
