from collections import defaultdict
from decimal import Decimal
from uuid import UUID

from app.repositories.memory_repository import AssetRepository, EntryRepository
from app.schemas.entry import WalletEntry
from app.schemas.wallet import WalletAllocationResponse, WalletPositionResponse, WalletSummaryResponse

_ZERO = Decimal(0)


class WalletService:
    def __init__(self, asset_repo: AssetRepository, entry_repo: EntryRepository) -> None:
        self._asset_repo = asset_repo
        self._entry_repo = entry_repo

    def get_positions(self) -> list[WalletPositionResponse]:
        """Return consolidated positions; last_unit_price uses the most recent entry by created_at."""
        all_entries = self._entry_repo.list_all()
        if not all_entries:
            return []

        grouped: dict[UUID, list[WalletEntry]] = defaultdict(list)
        for entry in all_entries:
            grouped[entry.asset_id].append(entry)

        positions: list[WalletPositionResponse] = []
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
            profit_loss_percentage = (profit_loss / invested_amount * 100) if invested_amount > _ZERO else _ZERO

            positions.append(WalletPositionResponse(
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

    def get_summary(self) -> WalletSummaryResponse:
        positions = self.get_positions()

        if not positions:
            return WalletSummaryResponse(
                total_assets=0,
                total_quantity=_ZERO,
                total_invested=_ZERO,
                total_current=_ZERO,
                total_profit_loss=_ZERO,
                total_profit_loss_percentage=_ZERO,
                allocation_by_asset_type=[],
            )

        total_invested = sum(p.invested_amount for p in positions)
        total_current = sum(p.current_amount for p in positions)
        total_profit_loss = total_current - total_invested
        total_profit_loss_percentage = (
            total_profit_loss / total_invested * 100 if total_invested > _ZERO else _ZERO
        )

        by_type: dict[str, Decimal] = defaultdict(lambda: _ZERO)
        for p in positions:
            by_type[p.asset_type] += p.current_amount

        allocation = [
            WalletAllocationResponse(
                asset_type=atype,
                current_amount=amount,
                percentage=(amount / total_current * 100) if total_current > _ZERO else _ZERO,
            )
            for atype, amount in by_type.items()
        ]

        return WalletSummaryResponse(
            total_assets=len(positions),
            total_quantity=sum(p.total_quantity for p in positions),
            total_invested=total_invested,
            total_current=total_current,
            total_profit_loss=total_profit_loss,
            total_profit_loss_percentage=total_profit_loss_percentage,
            allocation_by_asset_type=allocation,
        )
