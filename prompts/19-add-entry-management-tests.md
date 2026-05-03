# Prompt 19 - Criar testes automatizados para entradas/transações

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 3 - Entradas/Transações
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com CRUD de entradas e consistência entre ativo e entradas implementados.

### O - Objetivo
Criar testes automatizados para os fluxos principais de entradas/transações, incluindo consistência com ativos.

### S - Estilo
Testes simples, objetivos e legíveis. Garantir isolamento entre testes.

### T - Tom
Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a qualidade incremental do projeto.

### R - Resposta esperada
Testes cobrindo criação, listagem, remoção e consistência com ativos.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `tests/test_entries.py` | Criado — 11 testes para fluxos de entradas/transações |
| `prompts/19-add-entry-management-tests.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Cenários cobertos

| Teste | Comportamento verificado |
|---|---|
| `test_create_entry_returns_201` | POST retorna 201 |
| `test_create_entry_returns_expected_fields` | Resposta contém id, asset_id, quantity, unit_price, created_at |
| `test_create_entry_for_nonexistent_asset_returns_404` | POST com asset_id inexistente retorna 404 |
| `test_list_entries_returns_empty_list` | GET retorna `[]` sem entradas |
| `test_list_entries_returns_created_entries` | GET retorna entradas criadas |
| `test_delete_entry_returns_204` | DELETE retorna 204 |
| `test_delete_entry_removes_from_list` | Entrada deletada não aparece em GET |
| `test_delete_nonexistent_entry_returns_404` | DELETE com id desconhecido retorna 404 |
| `test_delete_asset_with_entries_returns_409` | DELETE de ativo com entradas retorna 409 |
| `test_delete_asset_allowed_after_entries_removed` | Após cancelar entradas, ativo pode ser removido (204) |

## Decisão técnica — fixture de isolamento

A fixture `reset_services` cria instâncias frescas de `AssetRepository` e `EntryRepository` e as injeta em ambos os services (`AssetService` e `EntryService`) via monkeypatch. Compartilhar os mesmos repositórios entre os dois services é obrigatório: sem isso, um ativo criado via `/assets/` não seria encontrado pela validação do `/entries/`, e a consistência entre ativo e entradas não poderia ser testada.

`AssetService` é instanciado com `entry_repo=fresh_entry_repo` para que a consistência (bloqueio de deleção com entradas) esteja ativa nos testes — diferente dos testes de asset que usam `AssetService()` sem `entry_repo`.
