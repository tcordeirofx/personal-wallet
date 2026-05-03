# Prompt 13 - Criar testes para validações de domínio de ativos

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 2 - Gestão de ativos
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com validações de domínio básicas de ativos implementadas: normalização uppercase e bloqueio de symbol duplicado.

### O - Objetivo
Criar testes automatizados apenas para as validações de domínio básicas de ativos.

### S - Estilo
Testes simples, objetivos e legíveis. Usar Pytest e FastAPI TestClient.

### T - Tom
Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a qualidade incremental do projeto.

### R - Resposta esperada
Testes para normalização uppercase e bloqueio de duplicata, com isolamento de estado entre testes.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `tests/test_asset_validations.py` | Criado — 6 testes para validações de domínio |
| `prompts/13-add-asset-domain-validation-tests.md` | Criado — este arquivo |

## Cenários cobertos

| Teste | Comportamento verificado |
|---|---|
| `test_symbol_normalized_to_uppercase` | "petr4" → armazenado e retornado como "PETR4" |
| `test_currency_normalized_to_uppercase` | "brl" → armazenado e retornado como "BRL" |
| `test_duplicate_symbol_returns_409` | Segundo POST com mesmo symbol retorna 409 com detail |
| `test_duplicate_symbol_is_case_insensitive` | "BBAS3" + "bbas3" → 409 (normalização torna ambos iguais) |
| `test_update_to_existing_symbol_returns_409` | PUT com symbol de outro ativo retorna 409 com detail |
| `test_update_own_symbol_is_allowed` | PUT com o próprio symbol retorna 200 |

## Decisão técnica — isolamento de estado

`_service` é um singleton a nível de módulo em `app/routers/assets.py`. Sem isolamento, ativos criados em um teste contaminam os seguintes. A fixture `reset_service` usa `monkeypatch.setattr` para substituir `_service` por uma instância fresca de `AssetService` antes de cada teste, sem tocar em código de produção.
