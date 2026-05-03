# Prompt 11 - Implementar remoção de ativo

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 2 - Gestão de ativos
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com cadastro, listagem e atualização de ativos implementados.

### O - Objetivo
Implementar apenas a remoção de ativo via `DELETE /assets/{asset_id}/`.

### S - Estilo
Código simples, tipado e legível. Manter separação entre router, service e repository.

### T - Tom
Mensagens claras e objetivas. Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a evolução incremental do projeto.

### R - Resposta esperada
`DELETE /assets/{asset_id}/` retornando HTTP 204 ou 404.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/services/asset_service.py` | Alterado — método `delete` adicionado |
| `app/routers/assets.py` | Alterado — endpoint `DELETE /{asset_id}/` adicionado |
| `prompts/11-add-asset-delete-endpoint.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Decisões técnicas

- **HTTP 204 com `Response(status_code=204)` explícito**: retornar `None` em um handler com `status_code=204` funciona, mas retornar `Response` diretamente é mais explícito e evita que o FastAPI tente serializar um body vazio com `response_model`.
- **`Response` importado de `fastapi`**: mesma origem dos outros imports do router, sem dependência nova.
- **Lógica de 404 no router**: `_service.delete` retorna `bool`; a decisão de converter `False` em HTTP 404 pertence à camada de apresentação, mantendo o service agnóstico ao protocolo HTTP.
