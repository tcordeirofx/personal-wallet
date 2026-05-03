# Prompt 06 - Criar endpoint de health check

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 1 - Estrutura base da API
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com FastAPI, schemas, camadas organizadas e repositórios em memória.

### O - Objetivo
Criar apenas o endpoint de health check da API.

### S - Estilo
Código simples e direto. Endpoint pequeno e sem dependências de domínio.

### T - Tom
Mensagens claras e objetivas.

### A - Audiência
Professor avaliador e desenvolvedores que validarão se a API sobe corretamente.

### R - Resposta esperada
`GET /health` retornando HTTP 200 com `{"status": "ok", "service": "personal-wallet-api"}`.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/main.py` | Alterado — endpoint `GET /health` adicionado |
| `prompts/06-add-health-check-endpoint.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Decisões técnicas

- **Endpoint direto em `main.py`**: health check não pertence a nenhum domínio de negócio; registrá-lo no app raiz é a convenção mais comum.
- **Retorno `dict`**: sem necessidade de schema Pydantic para uma resposta fixa e sem variação; FastAPI serializa `dict` diretamente.
- **Sem `status_code` explícito**: FastAPI usa 200 por padrão para `GET`; declarar seria redundante aqui.
