# Prompt 17 - Implementar remoção/cancelamento de entrada

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 3 - Entradas/Transações
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com `POST /entries/` e `GET /entries/` implementados na Release 3.

### O - Objetivo
Implementar apenas a remoção/cancelamento de entrada via `DELETE /entries/{entry_id}/`.

### S - Estilo
Código simples, tipado e legível. Manter separação entre router, service e repository.

### T - Tom
Mensagens claras e objetivas. Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a evolução incremental do projeto.

### R - Resposta esperada
`DELETE /entries/{entry_id}/` retornando HTTP 204 ou 404.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/services/entry_service.py` | Alterado — método `delete` adicionado |
| `app/routers/entries.py` | Alterado — endpoint `DELETE /{entry_id}/` adicionado |
| `prompts/17-add-entry-delete-endpoint.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Decisões técnicas

- Mesmo padrão do `DELETE /assets/{asset_id}/`: service retorna `bool`, router converte `False` em HTTP 404.
- `Response(status_code=204)` explícito evita que FastAPI tente serializar body vazio.
- A remoção cancela o lançamento — não representa venda nem altera posição calculada (isso é escopo da Release 4).
