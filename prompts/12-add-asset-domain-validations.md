# Prompt 12 - Adicionar validações de domínio básicas para ativo

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 2 - Gestão de ativos
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com CRUD completo de ativos e armazenamento em memória.

### O - Objetivo
Adicionar validações de domínio básicas: normalização de symbol/currency para uppercase e rejeição de symbol duplicado.

### S - Estilo
Código simples, tipado e legível. Validações de domínio no service; normalização nos schemas.

### T - Tom
Mensagens de erro claras e objetivas. Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a evolução incremental do projeto.

### R - Resposta esperada
Normalização uppercase nos schemas, verificação de duplicata no service, HTTP 409 no router.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/schemas/asset.py` | Alterado — `@field_validator` para uppercase em `symbol` e `currency` |
| `app/repositories/memory_repository.py` | Alterado — método `get_by_symbol` adicionado em `AssetRepository` |
| `app/services/asset_service.py` | Alterado — verificação de symbol duplicado em `create` e `update` |
| `app/routers/assets.py` | Alterado — `try/except ValueError` → HTTP 409 em `create_asset` e `update_asset` |
| `prompts/12-add-asset-domain-validations.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Decisões técnicas

- **Normalização via `@field_validator(mode="before")`**: aplicada nos schemas (`AssetCreate` e `AssetUpdate`) antes da validação de `min_length`, garantindo que "petr4" e "PETR4" sejam tratados identicamente em toda a pilha.
- **`get_by_symbol` no repositório**: busca por symbol sem expor a estrutura interna do store ao service; O(n) aceitável para MVP em memória.
- **Verificação de duplicata no service, não no repositório**: regra de negócio (unicidade de symbol) pertence ao domínio, não à camada de armazenamento.
- **`ValueError` no service → HTTP 409 no router**: o service permanece agnóstico a HTTP; a tradução de exceção de domínio para status code fica na camada de apresentação.
- **HTTP 409 Conflict** (não 400): semanticamente correto para conflito de recurso existente.
- **Update do próprio symbol não bloqueado**: a verificação `existing.id != asset_id` permite que um ativo atualize outros campos sem mudar o symbol, ou atualize o symbol para o mesmo valor sem ser bloqueado.
