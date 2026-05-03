# Prompt 20 - Implementar consulta de posições consolidadas

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 4 - Consultas de carteira
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com Releases 0-3 concluídas. `WalletService` e `app/routers/wallet.py` existem como stubs vazios desde a Release 1.

### O - Objetivo
Implementar apenas `GET /wallet/positions/` para consulta de posições consolidadas por ativo.

### S - Estilo
Código simples, tipado e legível. Cálculo no service. Sem cotação externa.

### T - Tom
Mensagens claras e objetivas. Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a evolução incremental do projeto.

### R - Resposta esperada
`GET /wallet/positions/` retornando lista de `AssetPosition` ou `[]`.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/schemas/wallet.py` | Criado — schema `AssetPosition` |
| `app/schemas/__init__.py` | Alterado — re-exporta `AssetPosition` |
| `app/services/wallet_service.py` | Alterado — `WalletService` implementado com `get_positions` |
| `app/routers/wallet.py` | Alterado — endpoint `GET /positions/` adicionado |
| `app/main.py` | Alterado — `wallet_router` registrado |
| `prompts/20-add-wallet-positions-endpoint.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Decisões técnicas

- **`defaultdict(list)` para agrupamento**: agrupa entradas por `asset_id` em O(n) sem múltiplas iterações.
- **`max(entries, key=lambda e: e.created_at)`** para `last_unit_price`: a entrada mais recente pelo timestamp UTC define o preço de referência atual; não depende de ordenação prévia.
- **`profit_loss_percentage = 0.0` quando `invested_amount == 0`**: guarda segura contra divisão por zero; matematicamente improvável com validação `quantity > 0` e `unit_price > 0`, mas explícita.
- **`if asset is None: continue`**: entrada órfã (ativo removido após cancelamento de todas as entradas não é possível pela consistência atual, mas a guarda é defensiva).
- **`WalletService(asset_repo, entry_repo)`**: mesmo padrão de injeção explícita dos outros services; usa os singletons de `dependencies.py`.
- **`float`** para campos monetários: consistente com os schemas de `AssetCreate`/`WalletEntryCreate`; precisão decimal pode ser revisada na Release 5.
