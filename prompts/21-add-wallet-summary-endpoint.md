# Prompt 21 - Implementar resumo geral da carteira

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 4 - Consultas de carteira
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com `GET /wallet/positions/` implementado. `WalletService.get_positions()` já calcula posições consolidadas.

### O - Objetivo
Implementar apenas `GET /wallet/summary/` para resumo geral da carteira.

### S - Estilo
Código simples, tipado e legível. Reaproveitar `get_positions()`. Sem duplicação de cálculo.

### T - Tom
Mensagens claras e objetivas. Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a evolução incremental do projeto.

### R - Resposta esperada
`GET /wallet/summary/` retornando `WalletSummary` com totais e alocação por tipo de ativo.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/schemas/wallet.py` | Alterado — `AllocationByType` e `WalletSummary` adicionados |
| `app/schemas/__init__.py` | Alterado — re-exporta `AllocationByType` e `WalletSummary` |
| `app/services/wallet_service.py` | Alterado — método `get_summary` adicionado |
| `app/routers/wallet.py` | Alterado — endpoint `GET /summary/` adicionado |
| `prompts/21-add-wallet-summary-endpoint.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Decisões técnicas

- **`get_summary` chama `get_positions()`**: toda a lógica de agrupamento e cálculo de posição já está encapsulada; o resumo apenas agrega os resultados — sem duplicação.
- **`defaultdict(float)` para `allocation_by_asset_type`**: agrupamento O(n) de `current_amount` por `asset_type`; o percentual é calculado sobre `total_current`.
- **Percentual `0.0` quando `total_current == 0`**: guarda defensiva para divisão por zero; improvável com validações existentes, mas explícita.
- **`WalletSummary` com totais zerados e lista vazia** quando sem posições: contrato claro para carteira vazia, sem necessidade de tratar 404.
