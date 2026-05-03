# Prompt 08 - Implementar cadastro de ativo

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 2 - Gestão de ativos
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com Release 1 concluída: FastAPI, schemas, camadas, repositórios em memória, /health e teste automatizado.

### O - Objetivo
Implementar apenas o cadastro de ativo via `POST /assets`.

### S - Estilo
Código simples, tipado e legível. Separação entre router, service e repository.

### T - Tom
Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a evolução incremental do projeto.

### R - Resposta esperada
`POST /assets` retornando HTTP 201 com o ativo criado, incluindo id gerado.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/services/asset_service.py` | Criado — `AssetService` com método `create` |
| `app/services/__init__.py` | Alterado — re-exporta `AssetService` |
| `app/routers/assets.py` | Alterado — endpoint `POST /` adicionado |
| `app/main.py` | Alterado — `assets_router` registrado no app |
| `prompts/08-add-asset-create-endpoint.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Decisões técnicas

- **`AssetService` separado de `WalletService`**: cada domínio tem seu próprio service; `WalletService` ficará para as consultas de carteira (Release 4).
- **Singleton `_service` a nível de módulo no router**: instância única compartilhada por todas as requisições; garante que o repositório em memória persista durante a vida do processo sem usar FastAPI DI neste momento.
- **`response_model=Asset`**: FastAPI filtra a resposta pelo schema, garantindo o contrato de saída independentemente do que o service retornar.
- **`status_code=201`** declarado no decorator: semântica REST correta para criação de recurso.
- **Rota registrada com prefixo `/assets`**: o decorator usa `"/"` e o `APIRouter` carrega o prefixo, resultando em `POST /assets`.
