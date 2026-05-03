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


def _create(symbol: str, currency: str = "BRL") -> dict:
    return client.post(
        BASE,
        json={"symbol": symbol, "name": f"Asset {symbol}", "asset_type": "stock", "currency": currency},
    )


def test_symbol_normalized_to_uppercase():
    response = _create("petr4")
    assert response.status_code == 201
    assert response.json()["symbol"] == "PETR4"


def test_currency_normalized_to_uppercase():
    response = _create("PETR4", currency="brl")
    assert response.status_code == 201
    assert response.json()["currency"] == "BRL"


def test_duplicate_symbol_returns_409():
    _create("VALE3")
    response = _create("VALE3")
    assert response.status_code == 409
    assert "VALE3" in response.json()["detail"]


def test_duplicate_symbol_is_case_insensitive():
    _create("BBAS3")
    response = _create("bbas3")
    assert response.status_code == 409


def test_update_to_existing_symbol_returns_409():
    asset_a = _create("ITUB4").json()
    _create("MGLU3")
    response = client.put(f"{BASE}{asset_a['id']}/", json={"symbol": "MGLU3"})
    assert response.status_code == 409
    assert "MGLU3" in response.json()["detail"]


def test_update_own_symbol_is_allowed():
    asset = _create("WEGE3").json()
    response = client.put(f"{BASE}{asset['id']}/", json={"symbol": "WEGE3"})
    assert response.status_code == 200
    assert response.json()["symbol"] == "WEGE3"
