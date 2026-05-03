# Prompt 25 - Cobrir cenários adicionais de erro e borda

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 5 - Qualidade e estabilização
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com 43 testes passando. Revisar lacunas de cobertura de erro e borda.

### O - Objetivo
Adicionar testes para cenários adicionais de erro e borda, sem criar novas funcionalidades.

### S - Estilo
Testes simples, objetivos. Sem duplicação dos cenários já cobertos.

### T - Tom
Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a qualidade final do projeto.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `tests/test_edge_cases.py` | Criado — 13 testes de erro e borda |
| `prompts/25-add-edge-case-tests.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Cenários cobertos

| Teste | Validação |
|---|---|
| `test_create_asset_with_empty_symbol_returns_422` | `min_length=1` no schema → 422 |
| `test_create_asset_with_empty_name_returns_422` | idem |
| `test_create_asset_with_empty_asset_type_returns_422` | idem |
| `test_create_asset_with_empty_currency_returns_422` | idem |
| `test_create_entry_with_zero_quantity_returns_422` | `Field(gt=0)` → 422 |
| `test_create_entry_with_negative_quantity_returns_422` | idem |
| `test_create_entry_with_zero_unit_price_returns_422` | `Field(gt=0)` → 422 |
| `test_create_entry_with_negative_unit_price_returns_422` | idem |
| `test_update_asset_with_empty_payload_returns_200` | PUT `{}` é válido → 200 |
| `test_update_asset_with_empty_payload_preserves_all_fields` | todos os campos permanecem inalterados |
| `test_positions_empty_when_asset_has_no_entries` | ativo sem entradas → positions `[]` |
| `test_summary_zeroed_when_asset_has_no_entries` | ativo sem entradas → summary zerado |

## Cenários não duplicados (já cobertos)

- `DELETE /entries/{id}` inexistente → `test_entries.py:test_delete_nonexistent_entry_returns_404`
- positions/summary sem nenhum ativo → `test_wallet.py:test_positions_empty_without_entries` e `test_summary_zeroed_without_positions`

## Bugs encontrados

Nenhum. Todos os comportamentos observados estão corretos:
- Pydantic valida `min_length` e `gt` antes de chegar ao handler → 422 automático.
- `AssetUpdate` com payload vazio usa `model_dump(exclude_none=True)` = `{}` → `model_copy(update={})` retorna o ativo inalterado.
- `WalletService.get_positions()` só processa ativos que têm entradas no `EntryRepository` → ativo sem entradas não aparece na posição.
