# Prompt 18 - Garantir consistência mínima entre ativo e entradas

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 3 - Entradas/Transações
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com CRUD de ativos e entradas implementados. A criação de entrada já valida `asset_id`. Falta bloquear remoção de ativo com entradas associadas.

### O - Objetivo
Garantir consistência mínima: impedir remoção de ativo que possui entradas associadas.

### S - Estilo
Código simples, tipado e legível. Regras de consistência no service.

### T - Tom
Mensagens claras e objetivas. Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a evolução incremental do projeto.

### R - Resposta esperada
`DELETE /assets/{asset_id}/` retornando HTTP 409 quando o ativo tiver entradas.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/services/asset_service.py` | Alterado — `__init__` aceita `entry_repo` opcional; `delete` verifica entradas |
| `app/routers/assets.py` | Alterado — `_service` passa `entry_repo`; `delete_asset` captura `ValueError` → 409 |
| `prompts/18-add-asset-entry-consistency.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Decisões técnicas

- **`entry_repo: EntryRepository | None = None` no `AssetService.__init__`**: parâmetro opcional garante que testes existentes `AssetService()` continuem funcionando sem entry checking (test isolation preservada). Em produção, `entry_repo=entry_repository` é passado pelo router.
- **Verificação em `delete` apenas quando `entry_repo` está presente**: quando `None`, o método se comporta como antes — não há regressão nos testes de asset que não configuram entry repo.
- **`entry_repo.list_by_asset`** já existia no `EntryRepository`; nenhuma mudança no repositório foi necessária.
- **HTTP 409** para ativo com entradas: conflito de estado, não recurso ausente.
- **Mensagem inclui contagem**: `"Asset '...' has N associated entries"` informa quantas entradas precisam ser canceladas.
