from datetime import datetime, timezone
from uuid import UUID, uuid4

from app.schemas.asset import Asset, AssetCreate, AssetUpdate
from app.schemas.entry import WalletEntry, WalletEntryCreate


class AssetRepository:
    """In-memory asset store. State is lost on process restart."""

    def __init__(self) -> None:
        self._store: dict[UUID, Asset] = {}

    def create(self, data: AssetCreate) -> Asset:
        asset = Asset(id=uuid4(), **data.model_dump())
        self._store[asset.id] = asset
        return asset

    def list_all(self) -> list[Asset]:
        return list(self._store.values())

    def get_by_id(self, id: UUID) -> Asset | None:
        return self._store.get(id)

    def get_by_symbol(self, symbol: str) -> Asset | None:
        return next((a for a in self._store.values() if a.symbol == symbol), None)

    def update(self, id: UUID, data: AssetUpdate) -> Asset | None:
        asset = self._store.get(id)
        if asset is None:
            return None
        updated = asset.model_copy(update=data.model_dump(exclude_none=True))
        self._store[id] = updated
        return updated

    def delete(self, id: UUID) -> bool:
        if id not in self._store:
            return False
        del self._store[id]
        return True


class EntryRepository:
    """In-memory entry store. State is lost on process restart."""

    def __init__(self) -> None:
        self._store: dict[UUID, WalletEntry] = {}

    def create(self, data: WalletEntryCreate) -> WalletEntry:
        entry = WalletEntry(
            id=uuid4(),
            created_at=datetime.now(timezone.utc),
            **data.model_dump(),
        )
        self._store[entry.id] = entry
        return entry

    def list_all(self) -> list[WalletEntry]:
        return list(self._store.values())

    def list_by_asset(self, asset_id: UUID) -> list[WalletEntry]:
        return [e for e in self._store.values() if e.asset_id == asset_id]

    def get_by_id(self, id: UUID) -> WalletEntry | None:
        return self._store.get(id)

    def delete(self, id: UUID) -> bool:
        if id not in self._store:
            return False
        del self._store[id]
        return True
