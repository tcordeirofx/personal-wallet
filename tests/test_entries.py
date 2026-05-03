import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

ASSETS = "/assets/"
ENTRIES = "/entries/"


@pytest.fixture(autouse=True)
def reset_services(monkeypatch):
    from app.repositories.memory_repository import AssetRepository, EntryRepository
    from app.routers import assets as assets_module
    from app.routers import entries as entries_module
    from app.services.asset_service import AssetService
    from app.services.entry_service import EntryService

    fresh_asset_repo = AssetRepository()
    fresh_entry_repo = EntryRepository()

    monkeypatch.setattr(
        assets_module,
        "_service",
        AssetService(repo=fresh_asset_repo, entry_repo=fresh_entry_repo),
    )
    monkeypatch.setattr(
        entries_module,
        "_service",
        EntryService(asset_repo=fresh_asset_repo, entry_repo=fresh_entry_repo),
    )


def _create_asset(symbol: str = "PETR4") -> dict:
    response = client.post(
        ASSETS,
        json={"symbol": symbol, "name": f"Asset {symbol}", "asset_type": "stock", "currency": "BRL"},
    )
    assert response.status_code == 201
    return response.json()


def _create_entry(asset_id: str, quantity: float = 10.0, unit_price: float = 32.5) -> dict:
    response = client.post(
        ENTRIES,
        json={"asset_id": asset_id, "quantity": quantity, "unit_price": unit_price},
    )
    assert response.status_code == 201
    return response.json()


# --- criação de entrada ---

def test_create_entry_returns_201():
    asset = _create_asset()
    response = client.post(
        ENTRIES,
        json={"asset_id": asset["id"], "quantity": 10, "unit_price": 32.5},
    )
    assert response.status_code == 201


def test_create_entry_returns_expected_fields():
    asset = _create_asset()
    entry = _create_entry(asset["id"])
    assert entry["asset_id"] == asset["id"]
    assert entry["quantity"] == 10.0
    assert entry["unit_price"] == 32.5
    assert "id" in entry
    assert "created_at" in entry


def test_create_entry_for_nonexistent_asset_returns_404():
    response = client.post(
        ENTRIES,
        json={"asset_id": "00000000-0000-0000-0000-000000000000", "quantity": 5, "unit_price": 10.0},
    )
    assert response.status_code == 404


# --- listagem de entradas ---

def test_list_entries_returns_empty_list():
    response = client.get(ENTRIES)
    assert response.status_code == 200
    assert response.json() == []


def test_list_entries_returns_created_entries():
    asset = _create_asset()
    _create_entry(asset["id"], quantity=5, unit_price=20.0)
    _create_entry(asset["id"], quantity=3, unit_price=25.0)
    response = client.get(ENTRIES)
    assert response.status_code == 200
    assert len(response.json()) == 2


# --- remoção de entrada ---

def test_delete_entry_returns_204():
    asset = _create_asset()
    entry = _create_entry(asset["id"])
    response = client.delete(f"{ENTRIES}{entry['id']}/")
    assert response.status_code == 204


def test_delete_entry_removes_from_list():
    asset = _create_asset()
    entry = _create_entry(asset["id"])
    client.delete(f"{ENTRIES}{entry['id']}/")
    ids = [e["id"] for e in client.get(ENTRIES).json()]
    assert entry["id"] not in ids


def test_delete_nonexistent_entry_returns_404():
    response = client.delete(f"{ENTRIES}00000000-0000-0000-0000-000000000000/")
    assert response.status_code == 404


# --- consistência entre ativo e entradas ---

def test_delete_asset_with_entries_returns_409():
    asset = _create_asset()
    _create_entry(asset["id"])
    response = client.delete(f"{ASSETS}{asset['id']}/")
    assert response.status_code == 409


def test_delete_asset_allowed_after_entries_removed():
    asset = _create_asset()
    entry = _create_entry(asset["id"])
    client.delete(f"{ENTRIES}{entry['id']}/")
    response = client.delete(f"{ASSETS}{asset['id']}/")
    assert response.status_code == 204
