# Prompt 10 - Implementar atualização de ativo

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 2 - Gestão de ativos
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com cadastro e listagem de ativos implementados.

### O - Objetivo
Implementar apenas a atualização de ativo via `PUT /assets/{asset_id}/`.

### S - Estilo
Código simples, tipado e legível. Manter separação entre router, service e repository.

### T - Tom
Mensagens claras e objetivas. Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a evolução incremental do projeto.

### R - Resposta esperada
`PUT /assets/{asset_id}/` com atualização parcial, HTTP 200 ou 404.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/services/asset_service.py` | Alterado — método `update` adicionado |
| `app/routers/assets.py` | Alterado — endpoint `PUT /{asset_id}/` adicionado |
| `prompts/10-add-asset-update-endpoint.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Decisões técnicas

- **`AssetUpdate` com campos opcionais**: permite atualização parcial — apenas os campos enviados no body são alterados; os demais permanecem inalterados (já implementado no `MemoryRepository.update` via `exclude_none=True`).
- **`HTTPException(404)`** no router, não no service: o service retorna `None` quando o id não existe; a decisão de transformar `None` em resposta HTTP pertence à camada de apresentação (router).
- **`UUID` como tipo do path parameter**: FastAPI valida e converte automaticamente a string do path para `uuid.UUID`; requisições com UUID malformado retornam HTTP 422 antes de chegar ao handler.
