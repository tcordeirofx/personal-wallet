from collections import defaultdict
from uuid import UUID

from app.repositories.memory_repository import AssetRepository, EntryRepository
from app.schemas.entry import WalletEntry
from app.schemas.wallet import AssetPosition


class WalletService:
    def __init__(self, asset_repo: AssetRepository, entry_repo: EntryRepository) -> None:
        self._asset_repo = asset_repo
        self._entry_repo = entry_repo

    def get_positions(self) -> list[AssetPosition]:
        all_entries = self._entry_repo.list_all()
        if not all_entries:
            return []

        grouped: dict[UUID, list[WalletEntry]] = defaultdict(list)
        for entry in all_entries:
            grouped[entry.asset_id].append(entry)

        positions: list[AssetPosition] = []
        for asset_id, entries in grouped.items():
            asset = self._asset_repo.get_by_id(asset_id)
            if asset is None:
                continue

            total_quantity = sum(e.quantity for e in entries)
            weighted_sum = sum(e.quantity * e.unit_price for e in entries)
            average_price = weighted_sum / total_quantity
            last_unit_price = max(entries, key=lambda e: e.created_at).unit_price
            invested_amount = total_quantity * average_price
            current_amount = total_quantity * last_unit_price
            profit_loss = current_amount - invested_amount
            profit_loss_percentage = (profit_loss / invested_amount * 100) if invested_amount > 0 else 0.0

            positions.append(AssetPosition(
                asset_id=asset.id,
                symbol=asset.symbol,
                name=asset.name,
                asset_type=asset.asset_type,
                currency=asset.currency,
                total_quantity=total_quantity,
                average_price=average_price,
                last_unit_price=last_unit_price,
                invested_amount=invested_amount,
                current_amount=current_amount,
                profit_loss=profit_loss,
                profit_loss_percentage=profit_loss_percentage,
            ))

        return positions
