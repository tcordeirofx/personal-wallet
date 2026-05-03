# Prompt 14 - Criar testes automatizados para gestão de ativos

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 2 - Gestão de ativos
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com CRUD de ativos e validações de domínio implementados. Já existem testes de validação em `test_asset_validations.py`.

### O - Objetivo
Criar testes automatizados para os fluxos principais de gestão de ativos.

### S - Estilo
Testes simples, objetivos e legíveis. Sem duplicação dos testes de validação já existentes.

### T - Tom
Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a qualidade incremental do projeto.

### R - Resposta esperada
Testes cobrindo cadastro, listagem, atualização parcial, remoção e erros 404.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `tests/test_assets.py` | Criado — 11 testes para fluxos principais de gestão de ativos |
| `prompts/14-add-asset-management-tests.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Cenários cobertos

| Teste | Comportamento verificado |
|---|---|
| `test_create_asset_returns_201` | POST retorna HTTP 201 |
| `test_create_asset_returns_expected_fields` | Resposta contém todos os campos esperados incluindo id |
| `test_list_assets_returns_empty_list` | GET retorna `[]` quando não há ativos |
| `test_list_assets_returns_created_assets` | GET retorna ativos criados |
| `test_update_asset_returns_200` | PUT retorna HTTP 200 |
| `test_update_asset_partial_changes_only_sent_fields` | PUT altera apenas o campo enviado, preserva os demais |
| `test_update_nonexistent_asset_returns_404` | PUT com id inexistente retorna HTTP 404 |
| `test_delete_asset_returns_204` | DELETE retorna HTTP 204 |
| `test_delete_asset_removes_from_list` | Ativo removido não aparece em GET |
| `test_delete_nonexistent_asset_returns_404` | DELETE com id inexistente retorna HTTP 404 |

## Decisão técnica — isolamento de estado

Mesmo padrão de `test_asset_validations.py`: fixture `reset_service(autouse=True)` usa `monkeypatch.setattr` para substituir `_service` por instância fresca antes de cada teste.

## Ajustes de código necessários

Nenhum. Os endpoints se comportaram exatamente como especificado.
