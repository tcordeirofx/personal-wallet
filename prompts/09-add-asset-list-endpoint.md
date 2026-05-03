# Prompt 09 - Implementar listagem de ativos

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 2 - Gestão de ativos
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com Release 1 concluída e `POST /assets/` implementado na Release 2.

### O - Objetivo
Implementar apenas a listagem de ativos via `GET /assets/`.

### S - Estilo
Código simples, tipado e legível. Manter separação entre router, service e repository.

### T - Tom
Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a evolução incremental do projeto.

### R - Resposta esperada
`GET /assets/` retornando HTTP 200 com lista de ativos (ou `[]` se vazia).

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/services/asset_service.py` | Alterado — método `list_all` adicionado |
| `app/routers/assets.py` | Alterado — endpoint `GET /` adicionado antes do `POST /` |
| `prompts/09-add-asset-list-endpoint.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Decisões técnicas

- **`GET /` antes do `POST /` no router**: ordem de declaração não afeta o roteamento do FastAPI, mas a convenção de listar o GET de coleção antes do POST é mais legível.
- **`response_model=list[Asset]`**: FastAPI serializa e valida a lista pelo schema; retorna `[]` automaticamente quando o repositório está vazio.
- **Nenhuma paginação**: o MVP não exige; seria prematura nesta etapa.
