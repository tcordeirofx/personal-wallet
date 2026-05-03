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


def _create_asset(symbol: str = "PETR4") -> dict:
    response = client.post(
        ASSETS,
        json={"symbol": symbol, "name": f"Asset {symbol}", "asset_type": "stock", "currency": "BRL"},
    )
    assert response.status_code == 201
    return response.json()


# --- campos obrigatórios de ativo ---

def test_create_asset_with_empty_symbol_returns_422():
    response = client.post(
        ASSETS,
        json={"symbol": "", "name": "Petrobras PN", "asset_type": "stock", "currency": "BRL"},
    )
    assert response.status_code == 422


def test_create_asset_with_empty_name_returns_422():
    response = client.post(
        ASSETS,
        json={"symbol": "PETR4", "name": "", "asset_type": "stock", "currency": "BRL"},
    )
    assert response.status_code == 422


def test_create_asset_with_empty_asset_type_returns_422():
    response = client.post(
        ASSETS,
        json={"symbol": "PETR4", "name": "Petrobras PN", "asset_type": "", "currency": "BRL"},
    )
    assert response.status_code == 422


def test_create_asset_with_empty_currency_returns_422():
    response = client.post(
        ASSETS,
        json={"symbol": "PETR4", "name": "Petrobras PN", "asset_type": "stock", "currency": ""},
    )
    assert response.status_code == 422


# --- campos numéricos de entrada ---

def test_create_entry_with_zero_quantity_returns_422():
    asset = _create_asset()
    response = client.post(
        ENTRIES,
        json={"asset_id": asset["id"], "quantity": 0, "unit_price": 32.5},
    )
    assert response.status_code == 422


def test_create_entry_with_negative_quantity_returns_422():
    asset = _create_asset()
    response = client.post(
        ENTRIES,
        json={"asset_id": asset["id"], "quantity": -1, "unit_price": 32.5},
    )
    assert response.status_code == 422


def test_create_entry_with_zero_unit_price_returns_422():
    asset = _create_asset()
    response = client.post(
        ENTRIES,
        json={"asset_id": asset["id"], "quantity": 10, "unit_price": 0},
    )
    assert response.status_code == 422


def test_create_entry_with_negative_unit_price_returns_422():
    asset = _create_asset()
    response = client.post(
        ENTRIES,
        json={"asset_id": asset["id"], "quantity": 10, "unit_price": -5.0},
    )
    assert response.status_code == 422


# --- atualização parcial com payload vazio ---

def test_update_asset_with_empty_payload_returns_200():
    asset = _create_asset()
    response = client.put(f"{ASSETS}{asset['id']}/", json={})
    assert response.status_code == 200


def test_update_asset_with_empty_payload_preserves_all_fields():
    asset = _create_asset()
    updated = client.put(f"{ASSETS}{asset['id']}/", json={}).json()
    assert updated["symbol"] == asset["symbol"]
    assert updated["name"] == asset["name"]
    assert updated["asset_type"] == asset["asset_type"]
    assert updated["currency"] == asset["currency"]
    assert updated["id"] == asset["id"]


# --- wallet com ativo cadastrado mas sem entradas ---

def test_positions_empty_when_asset_has_no_entries():
    _create_asset()
    response = client.get(POSITIONS)
    assert response.status_code == 200
    assert response.json() == []


def test_summary_zeroed_when_asset_has_no_entries():
    _create_asset()
    body = client.get(SUMMARY).json()
    assert body["total_assets"] == 0
    assert body["total_quantity"] == 0.0
    assert body["total_invested"] == 0.0
    assert body["total_current"] == 0.0
    assert body["total_profit_loss"] == 0.0
    assert body["allocation_by_asset_type"] == []
