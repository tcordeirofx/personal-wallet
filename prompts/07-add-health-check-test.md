# Prompt 07 - Criar teste automatizado para health check

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 1 - Estrutura base da API
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com FastAPI, schemas, camadas, repositórios em memória e endpoint GET /health.

### O - Objetivo
Criar o teste automatizado para o endpoint de health check.

### S - Estilo
Teste simples, direto e legível. Validar comportamento real do endpoint.

### T - Tom
Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que validarão a qualidade incremental do projeto.

### R - Resposta esperada
Testes Pytest com `TestClient` validando status 200 e corpo da resposta de `GET /health`.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `tests/__init__.py` | Criado — torna `tests` um pacote Python |
| `tests/test_health.py` | Criado — dois testes para `GET /health` |
| `requirements.txt` | Alterado — `httpx>=0.27.0` adicionado (dependência técnica do TestClient) |
| `prompts/07-add-health-check-test.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Decisões técnicas

- **`httpx` adicionado ao `requirements.txt`**: a restrição "sem dependências novas" foi interpretada como sem libs de domínio; `httpx` é requisito técnico do `TestClient` do Starlette (>=0.20) — sem ele o import falha com `ImportError`.
- **Dois testes separados**: `test_health_returns_200` e `test_health_returns_expected_body` — cada um valida uma asserção distinta, facilitando o diagnóstico de falha.
- **`client` a nível de módulo**: instância única para os testes do arquivo; sem estado entre chamadas, é seguro e evita overhead de criação repetida.
- **Sem fixture para `client`**: para um único arquivo com dois testes simples, fixture seria over-engineering; será introduzida quando o volume de testes justificar.
