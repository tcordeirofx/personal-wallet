# Prompt 15 - Implementar registro de entrada/transação

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 3 - Entradas/Transações
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com Release 2 concluída. Repositórios `AssetRepository` e `EntryRepository` já existem.

### O - Objetivo
Implementar apenas o endpoint `POST /entries/` para registrar entradas associadas a ativos existentes.

### S - Estilo
Código simples, tipado e legível. Manter separação entre router, service e repository.

### T - Tom
Mensagens claras e objetivas. Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a evolução incremental do projeto.

### R - Resposta esperada
`POST /entries/` retornando HTTP 201 com a entrada criada ou HTTP 404 se o ativo não existir.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/dependencies.py` | Criado — singletons `asset_repository` e `entry_repository` |
| `app/services/asset_service.py` | Alterado — `__init__` aceita `repo` opcional para injeção |
| `app/services/entry_service.py` | Criado — `EntryService` com método `create` |
| `app/services/__init__.py` | Alterado — re-exporta `EntryService` |
| `app/routers/assets.py` | Alterado — usa `AssetService(repo=asset_repository)` |
| `app/routers/entries.py` | Alterado — endpoint `POST /` adicionado |
| `app/main.py` | Alterado — `entries_router` registrado |
| `prompts/15-add-entry-create-endpoint.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Decisões técnicas

- **`app/dependencies.py` com singletons**: `asset_repository` e `entry_repository` são instâncias únicas compartilhadas por toda a aplicação. Ambos os routers importam deste módulo, garantindo que `EntryService` valide assets no mesmo store que `AssetService` gerencia.
- **`AssetService(repo=None)`**: o parâmetro opcional mantém compatibilidade total com os testes existentes — `AssetService()` sem argumento cria repositório fresco (test isolation preservada).
- **`EntryService` recebe `asset_repo` explicitamente**: a dependência é declarada no construtor, tornando o wiring visível e testável sem magia de framework.
- **HTTP 404 para asset não encontrado**: a entrada só existe em relação a um ativo; asset inexistente é um recurso não encontrado, não um conflito.
- **`created_at` gerado no repositório**: o chamador não precisa fornecer timestamp; o `EntryRepository.create` usa `datetime.now(timezone.utc)`.
