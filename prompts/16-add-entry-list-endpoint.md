# Prompt 16 - Implementar listagem de histórico de entradas

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 3 - Entradas/Transações
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com `POST /entries/` implementado na Release 3.

### O - Objetivo
Implementar apenas a listagem do histórico de entradas via `GET /entries/`.

### S - Estilo
Código simples, tipado e legível. Manter separação entre router, service e repository.

### T - Tom
Mensagens claras e objetivas. Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a evolução incremental do projeto.

### R - Resposta esperada
`GET /entries/` retornando HTTP 200 com lista de entradas (ou `[]` se vazia).

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/services/entry_service.py` | Alterado — método `list_all` adicionado |
| `app/routers/entries.py` | Alterado — endpoint `GET /` adicionado antes do `POST /` |
| `prompts/16-add-entry-list-endpoint.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Decisões técnicas

- **`GET /` antes do `POST /` no router**: convenção de listar o endpoint de leitura de coleção antes do de criação.
- **`response_model=list[WalletEntry]`**: FastAPI serializa e valida cada item; retorna `[]` automaticamente quando o repositório está vazio.
- Sem paginação: fora do escopo do MVP.
