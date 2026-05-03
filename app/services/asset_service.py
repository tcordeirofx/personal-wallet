from app.repositories.memory_repository import AssetRepository
from app.schemas.asset import Asset, AssetCreate


class AssetService:
    def __init__(self) -> None:
        self._repo = AssetRepository()

    def create(self, data: AssetCreate) -> Asset:
        return self._repo.create(data)
