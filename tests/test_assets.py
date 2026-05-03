import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

BASE = "/assets/"


@pytest.fixture(autouse=True)
def reset_service(monkeypatch):
    from app.routers import assets as assets_module
    from app.services.asset_service import AssetService

    monkeypatch.setattr(assets_module, "_service", AssetService())


def _create(symbol: str = "PETR4") -> dict:
    response = client.post(
        BASE,
        json={"symbol": symbol, "name": f"Asset {symbol}", "asset_type": "stock", "currency": "BRL"},
    )
    assert response.status_code == 201
    return response.json()


# --- cadastro ---

def test_create_asset_returns_201():
    response = client.post(
        BASE,
        json={"symbol": "PETR4", "name": "Petrobras PN", "asset_type": "stock", "currency": "BRL"},
    )
    assert response.status_code == 201


def test_create_asset_returns_expected_fields():
    asset = _create("VALE3")
    assert asset["symbol"] == "VALE3"
    assert asset["name"] == "Asset VALE3"
    assert asset["asset_type"] == "stock"
    assert asset["currency"] == "BRL"
    assert "id" in asset


# --- listagem ---

def test_list_assets_returns_empty_list():
    response = client.get(BASE)
    assert response.status_code == 200
    assert response.json() == []


def test_list_assets_returns_created_assets():
    _create("PETR4")
    _create("VALE3")
    response = client.get(BASE)
    assert response.status_code == 200
    symbols = [a["symbol"] for a in response.json()]
    assert "PETR4" in symbols
    assert "VALE3" in symbols


# --- atualização ---

def test_update_asset_returns_200():
    asset = _create()
    response = client.put(f"{BASE}{asset['id']}/", json={"name": "Petrobras Preferencial"})
    assert response.status_code == 200


def test_update_asset_partial_changes_only_sent_fields():
    asset = _create()
    response = client.put(f"{BASE}{asset['id']}/", json={"name": "Novo Nome"})
    updated = response.json()
    assert updated["name"] == "Novo Nome"
    assert updated["symbol"] == asset["symbol"]
    assert updated["currency"] == asset["currency"]


def test_update_nonexistent_asset_returns_404():
    response = client.put(
        f"{BASE}00000000-0000-0000-0000-000000000000/",
        json={"name": "X"},
    )
    assert response.status_code == 404


# --- remoção ---

def test_delete_asset_returns_204():
    asset = _create()
    response = client.delete(f"{BASE}{asset['id']}/")
    assert response.status_code == 204


def test_delete_asset_removes_from_list():
    asset = _create()
    client.delete(f"{BASE}{asset['id']}/")
    ids = [a["id"] for a in client.get(BASE).json()]
    assert asset["id"] not in ids


def test_delete_nonexistent_asset_returns_404():
    response = client.delete(f"{BASE}00000000-0000-0000-0000-000000000000/")
    assert response.status_code == 404
