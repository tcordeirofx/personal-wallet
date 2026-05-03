from fastapi import FastAPI

app = FastAPI(
    title="Personal Wallet API",
    description="Micro API offline para controle de carteira de ativos de renda variável.",
    version="0.1.0",
)
