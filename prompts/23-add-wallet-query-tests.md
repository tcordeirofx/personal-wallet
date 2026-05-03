# Prompt 23 - Criar testes automatizados para consultas de carteira

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 4 - Consultas de carteira
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com `GET /wallet/positions/` e `GET /wallet/summary/` implementados com contratos formais.

### O - Objetivo
Criar testes automatizados para os endpoints de consulta da carteira, incluindo cálculos.

### S - Estilo
Testes simples, objetivos e legíveis. Isolamento entre testes. `pytest.approx` para floats.

### T - Tom
Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a qualidade incremental do projeto.

### R - Resposta esperada
Testes cobrindo posições, cálculos individuais, summary e allocation.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `tests/test_wallet.py` | Criado — 14 testes para endpoints de consulta da carteira |
| `prompts/23-add-wallet-query-tests.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Cenários cobertos

| Teste | Comportamento verificado |
|---|---|
| `test_positions_empty_without_entries` | GET /positions/ retorna `[]` sem entradas |
| `test_positions_one_position_after_entry` | GET /positions/ retorna 1 posição com symbol correto |
| `test_positions_total_quantity` | 10 + 5 = 15.0 |
| `test_positions_average_price` | (10×30 + 5×36) / 15 = 32.0 |
| `test_positions_last_unit_price_is_most_recent` | Entrada mais recente define preço = 36.0 |
| `test_positions_invested_amount` | 15 × 32.0 = 480.0 |
| `test_positions_current_amount` | 15 × 36.0 = 540.0 |
| `test_positions_profit_loss` | 540.0 − 480.0 = 60.0 |
| `test_positions_profit_loss_percentage` | 60.0 / 480.0 × 100 = 12.5% |
| `test_summary_zeroed_without_positions` | GET /summary/ retorna todos zeros e allocation `[]` |
| `test_summary_total_assets` | 2 ativos com entradas → total_assets = 2 |
| `test_summary_aggregated_totals` | totais corretos de qty, invested, current, P/L e pct |
| `test_summary_allocation_by_asset_type` | stock=20%, fii=80% sobre total_current=5000 |

## Decisão técnica — fixture e isolamento

A fixture `reset_services` cria `AssetRepository` e `EntryRepository` frescos e os injeta nos três services (assets, entries, wallet) via monkeypatch. Compartilhar os mesmos repositórios é obrigatório: sem isso, ativos criados via `/assets/` não seriam encontrados pelo `WalletService`.

`pytest.approx` é usado em todas as comparações float para tolerância a erros de ponto flutuante, sem necessidade de dependência nova.
