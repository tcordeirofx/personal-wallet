# Prompt 22 - Revisar contratos de resposta dos endpoints de consulta

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 4 - Consultas de carteira
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com `GET /wallet/positions/` e `GET /wallet/summary/` implementados usando schemas `AssetPosition`, `AllocationByType` e `WalletSummary`.

### O - Objetivo
Revisar e formalizar os contratos de resposta com nomes `*Response` consistentes.

### S - Estilo
Código simples, tipado e legível. Sem refatoração ampla. Apenas renomeação de schemas.

### T - Tom
Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão contratos e documentação da API.

### R - Resposta esperada
Schemas renomeados para `WalletPositionResponse`, `WalletAllocationResponse` e `WalletSummaryResponse`.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/schemas/wallet.py` | Alterado — classes renomeadas para convenção `*Response` |
| `app/schemas/__init__.py` | Alterado — re-exporta os nomes novos |
| `app/services/wallet_service.py` | Alterado — importações e anotações de tipo atualizadas |
| `app/routers/wallet.py` | Alterado — importações e `response_model` atualizados |
| `prompts/22-review-wallet-response-contracts.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Contratos revisados

| Schema antigo | Schema novo | Mudança |
|---|---|---|
| `AssetPosition` | `WalletPositionResponse` | Renomeação |
| `AllocationByType` | `WalletAllocationResponse` | Renomeação |
| `WalletSummary` | `WalletSummaryResponse` | Renomeação |

Campos, tipos e cálculos: **inalterados**.

## Decisão técnica

A convenção `*Response` alinha os schemas de saída da wallet ao padrão `*Create`/`*Update` já usado nos schemas de assets e entries, tornando o papel de cada schema imediatamente legível pelo nome. Nenhuma lógica foi alterada — apenas identidades de classe.
