# Prompt 02 - Criar estrutura inicial da aplicação FastAPI

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 1 - Estrutura base da API
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Você é o agente de desenvolvimento do projeto Personal Wallet API.

Este projeto faz parte de um desafio acadêmico cujo objetivo é demonstrar o uso de GenAI no desenvolvimento de software de forma incremental, documentada, testável e versionada.

O repositório já possui documentação inicial, backlog, arquitetura mínima, template de prompt CO-STAR e .gitignore.

Produto:
Personal Wallet API é uma micro API offline para controle simples de uma carteira de ativos de renda variável.

Stack planejada:
- Python
- FastAPI
- Pydantic
- Pytest
- armazenamento em memória

### O - Objetivo
Criar apenas a estrutura inicial mínima da aplicação FastAPI.

### S - Estilo
- Estrutura simples e incremental.
- Código mínimo e legível.
- Não implementar funcionalidades de domínio nesta etapa.
- Não criar endpoints de negócio.
- Não antecipar models, services ou repositories.

### T - Tom
- Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a evolução incremental do projeto.

### R - Resposta esperada
Crie ou altere apenas:
- app/__init__.py
- app/main.py
- requirements.txt
- Makefile
- prompts/02-create-fastapi-structure.md
- docs/backlog-releases.md

Implementação esperada:
- Criar uma instância básica de FastAPI em app/main.py.
- Criar requirements.txt com dependências mínimas para FastAPI, Uvicorn e Pytest.
- Criar Makefile com comandos básicos: install, run e test.
- Registrar este prompt em prompts/02-create-fastapi-structure.md.
- Atualizar docs/backlog-releases.md apenas para marcar como concluído o item:
  - [ ] Criar estrutura inicial da aplicação FastAPI.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/__init__.py` | Criado — pacote Python vazio |
| `app/main.py` | Criado — instância FastAPI com título, descrição e versão |
| `requirements.txt` | Criado — fastapi, uvicorn[standard], pytest |
| `Makefile` | Criado — targets: install, run, test |
| `prompts/02-create-fastapi-structure.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox do item desta etapa marcado como concluído |

## Decisões técnicas

- `uvicorn[standard]` inclui dependências extras (websockets, watchfiles) necessárias para `--reload` funcionar corretamente.
- `app/__init__.py` vazio para tornar `app` um pacote Python importável pelo Uvicorn.
- Sem nenhum endpoint definido em `app/main.py`; o FastAPI gera automaticamente `/docs` (Swagger UI) e `/openapi.json`.
