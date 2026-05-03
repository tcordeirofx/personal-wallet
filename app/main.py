from fastapi import FastAPI

from app.routers.assets import router as assets_router
from app.routers.entries import router as entries_router
from app.routers.wallet import router as wallet_router

app = FastAPI(
    title="Personal Wallet API",
    description="Micro API offline para controle de carteira de ativos de renda variável.",
    version="0.1.0",
)

app.include_router(assets_router)
app.include_router(entries_router)
app.include_router(wallet_router)


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "personal-wallet-api"}
