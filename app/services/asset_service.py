from uuid import UUID

from app.repositories.memory_repository import AssetRepository
from app.schemas.asset import Asset, AssetCreate, AssetUpdate


class AssetService:
    def __init__(self) -> None:
        self._repo = AssetRepository()

    def create(self, data: AssetCreate) -> Asset:
        return self._repo.create(data)

    def list_all(self) -> list[Asset]:
        return self._repo.list_all()

    def update(self, asset_id: UUID, data: AssetUpdate) -> Asset | None:
        return self._repo.update(asset_id, data)
