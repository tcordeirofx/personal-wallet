import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

ASSETS = "/assets/"
ENTRIES = "/entries/"
POSITIONS = "/wallet/positions/"
SUMMARY = "/wallet/summary/"


@pytest.fixture(autouse=True)
def reset_services(monkeypatch):
    from app.repositories.memory_repository import AssetRepository, EntryRepository
    from app.routers import assets as assets_module
    from app.routers import entries as entries_module
    from app.routers import wallet as wallet_module
    from app.services.asset_service import AssetService
    from app.services.entry_service import EntryService
    from app.services.wallet_service import WalletService

    fresh_asset_repo = AssetRepository()
    fresh_entry_repo = EntryRepository()

    monkeypatch.setattr(
        assets_module, "_service",
        AssetService(repo=fresh_asset_repo, entry_repo=fresh_entry_repo),
    )
    monkeypatch.setattr(
        entries_module, "_service",
        EntryService(asset_repo=fresh_asset_repo, entry_repo=fresh_entry_repo),
    )
    monkeypatch.setattr(
        wallet_module, "_service",
        WalletService(asset_repo=fresh_asset_repo, entry_repo=fresh_entry_repo),
    )


def _create_asset(symbol: str, asset_type: str = "stock") -> dict:
    response = client.post(
        ASSETS,
        json={"symbol": symbol, "name": f"Asset {symbol}", "asset_type": asset_type, "currency": "BRL"},
    )
    assert response.status_code == 201
    return response.json()


def _create_entry(asset_id: str, quantity: float, unit_price: float) -> dict:
    response = client.post(
        ENTRIES,
        json={"asset_id": asset_id, "quantity": quantity, "unit_price": unit_price},
    )
    assert response.status_code == 201
    return response.json()


# --- positions ---

def test_positions_empty_without_entries():
    response = client.get(POSITIONS)
    assert response.status_code == 200
    assert response.json() == []


def test_positions_one_position_after_entry():
    asset = _create_asset("PETR4")
    _create_entry(asset["id"], 10, 30.0)
    positions = client.get(POSITIONS).json()
    assert len(positions) == 1
    assert positions[0]["symbol"] == "PETR4"


def test_positions_total_quantity():
    asset = _create_asset("PETR4")
    _create_entry(asset["id"], 10, 30.0)
    _create_entry(asset["id"], 5, 36.0)
    pos = client.get(POSITIONS).json()[0]
    assert pos["total_quantity"] == pytest.approx(15.0)


def test_positions_average_price():
    # (10 * 30.0 + 5 * 36.0) / 15 = 480 / 15 = 32.0
    asset = _create_asset("PETR4")
    _create_entry(asset["id"], 10, 30.0)
    _create_entry(asset["id"], 5, 36.0)
    pos = client.get(POSITIONS).json()[0]
    assert pos["average_price"] == pytest.approx(32.0)


def test_positions_last_unit_price_is_most_recent():
    # second entry is created after first → last_unit_price = 36.0
    asset = _create_asset("PETR4")
    _create_entry(asset["id"], 10, 30.0)
    _create_entry(asset["id"], 5, 36.0)
    pos = client.get(POSITIONS).json()[0]
    assert pos["last_unit_price"] == pytest.approx(36.0)


def test_positions_invested_amount():
    # invested_amount = total_quantity * average_price = 15 * 32.0 = 480.0
    asset = _create_asset("PETR4")
    _create_entry(asset["id"], 10, 30.0)
    _create_entry(asset["id"], 5, 36.0)
    pos = client.get(POSITIONS).json()[0]
    assert pos["invested_amount"] == pytest.approx(480.0)


def test_positions_current_amount():
    # current_amount = total_quantity * last_unit_price = 15 * 36.0 = 540.0
    asset = _create_asset("PETR4")
    _create_entry(asset["id"], 10, 30.0)
    _create_entry(asset["id"], 5, 36.0)
    pos = client.get(POSITIONS).json()[0]
    assert pos["current_amount"] == pytest.approx(540.0)


def test_positions_profit_loss():
    # profit_loss = 540.0 - 480.0 = 60.0
    asset = _create_asset("PETR4")
    _create_entry(asset["id"], 10, 30.0)
    _create_entry(asset["id"], 5, 36.0)
    pos = client.get(POSITIONS).json()[0]
    assert pos["profit_loss"] == pytest.approx(60.0)


def test_positions_profit_loss_percentage():
    # profit_loss_pct = 60.0 / 480.0 * 100 = 12.5
    asset = _create_asset("PETR4")
    _create_entry(asset["id"], 10, 30.0)
    _create_entry(asset["id"], 5, 36.0)
    pos = client.get(POSITIONS).json()[0]
    assert pos["profit_loss_percentage"] == pytest.approx(12.5)


# --- summary ---

def test_summary_zeroed_without_positions():
    response = client.get(SUMMARY)
    assert response.status_code == 200
    body = response.json()
    assert body["total_assets"] == 0
    assert body["total_quantity"] == 0.0
    assert body["total_invested"] == 0.0
    assert body["total_current"] == 0.0
    assert body["total_profit_loss"] == 0.0
    assert body["total_profit_loss_percentage"] == 0.0
    assert body["allocation_by_asset_type"] == []


def test_summary_total_assets():
    asset1 = _create_asset("PETR4", "stock")
    asset2 = _create_asset("KNRI11", "fii")
    _create_entry(asset1["id"], 100, 10.0)
    _create_entry(asset2["id"], 100, 40.0)
    assert client.get(SUMMARY).json()["total_assets"] == 2


def test_summary_aggregated_totals():
    # PETR4: qty=10, price=30→36. invested=480, current=540, P/L=60 (12.5%)
    asset = _create_asset("PETR4")
    _create_entry(asset["id"], 10, 30.0)
    _create_entry(asset["id"], 5, 36.0)
    body = client.get(SUMMARY).json()
    assert body["total_quantity"] == pytest.approx(15.0)
    assert body["total_invested"] == pytest.approx(480.0)
    assert body["total_current"] == pytest.approx(540.0)
    assert body["total_profit_loss"] == pytest.approx(60.0)
    assert body["total_profit_loss_percentage"] == pytest.approx(12.5)


def test_summary_allocation_by_asset_type():
    # stock: 100 * 10.0 = 1000 (20%), fii: 100 * 40.0 = 4000 (80%)
    asset1 = _create_asset("PETR4", "stock")
    asset2 = _create_asset("KNRI11", "fii")
    _create_entry(asset1["id"], 100, 10.0)
    _create_entry(asset2["id"], 100, 40.0)
    allocation = {
        a["asset_type"]: a
        for a in client.get(SUMMARY).json()["allocation_by_asset_type"]
    }
    assert allocation["stock"]["current_amount"] == pytest.approx(1000.0)
    assert allocation["stock"]["percentage"] == pytest.approx(20.0)
    assert allocation["fii"]["current_amount"] == pytest.approx(4000.0)
    assert allocation["fii"]["percentage"] == pytest.approx(80.0)
