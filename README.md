# Personal Wallet API

API offline para controle simples de carteira de ativos de renda variável.

## Problema resolvido

Controlar uma carteira de renda variável exige rastrear ativos, registrar compras e calcular posições consolidadas. Esta API resolve esse problema de forma simples, local e sem dependências externas: instale, rode e use.

## Objetivo do MVP

Demonstrar, em contexto acadêmico, o desenvolvimento incremental de uma micro API com separação de responsabilidades, testes automatizados e uso de IA generativa no processo de desenvolvimento.

O MVP suporta:
- gestão completa de ativos (CRUD com validações de domínio);
- registro, listagem e cancelamento de entradas/transações;
- consulta de posições consolidadas e resumo geral da carteira.

Todo o armazenamento é em memória. Ao reiniciar a API, os dados são perdidos — comportamento esperado para este MVP.

## Documentação do projeto

| Artefato | Arquivo | Conteúdo |
|---|---|---|
| Índice da documentação | [`docs/`](docs/README.md) | Ponto de entrada para todos os artefatos técnicos |
| Escopo do MVP | [`docs/escopo-MVP.md`](docs/escopo-MVP.md) | Funcionalidades implementadas, premissas e limites |
| Requisitos | [`docs/requisitos.md`](docs/requisitos.md) | RF, RNF, regras de negócio, fora de escopo e critérios de aceite |
| Backlog | [`docs/backlog-releases.md`](docs/backlog-releases.md) | Evolução incremental por release com checkboxes |
| Arquitetura | [`docs/arquitetura-componentes.md`](docs/arquitetura-componentes.md) | Diagrama e explicação das camadas da aplicação |
| Revisão final | [`docs/revisao-final.md`](docs/revisao-final.md) | Avaliação crítica da entrega: escopo, qualidade, testes, limitações e próximos passos |
| Prompts | [`prompts/`](prompts/README.md) | Índice comentado de todos os prompts CO-STAR usados no desenvolvimento |

## Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3.11+ | Linguagem principal |
| FastAPI | Framework web e geração automática de OpenAPI/Swagger |
| Pydantic | Validação e contratos de schemas |
| Uvicorn | Servidor ASGI |
| Pytest | Testes automatizados |
| httpx | Client HTTP para testes com TestClient |

## Pré-requisitos

- Python 3.11 ou superior
- make

Validar o ambiente:

```bash
python3 --version
make --version
```

## Instalação

```bash
git clone <url-do-repositorio>
cd personal-wallet
make install
```

`make install` cria `.venv/` automaticamente caso não exista e instala as dependências dentro dele.

## Execução

```bash
make run
# API disponível em http://127.0.0.1:8000
```

## Testes

```bash
make test
# 56 testes — health, assets, entries, wallet, edge cases
```

## Documentação interativa

Com a API em execução:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

## Endpoints

### Health

| Método | Rota | Status |
|---|---|---|
| GET | `/health` | 200 |

### Ativos

| Método | Rota | Sucesso | Erros |
|---|---|---|---|
| GET | `/assets/` | 200 | — |
| POST | `/assets/` | 201 | 409 (symbol duplicado), 422 (dados inválidos) |
| PUT | `/assets/{asset_id}/` | 200 | 404 (não encontrado), 409 (symbol duplicado) |
| DELETE | `/assets/{asset_id}/` | 204 | 404 (não encontrado), 409 (tem entradas associadas) |

### Entradas

| Método | Rota | Sucesso | Erros |
|---|---|---|---|
| GET | `/entries/` | 200 | — |
| POST | `/entries/` | 201 | 404 (ativo não encontrado), 422 (dados inválidos) |
| DELETE | `/entries/{entry_id}/` | 204 | 404 (não encontrada) |

### Carteira

| Método | Rota | Sucesso |
|---|---|---|
| GET | `/wallet/positions/` | 200 |
| GET | `/wallet/summary/` | 200 |

## Exemplos de uso

### Cadastrar ativo

```bash
curl -s -X POST http://127.0.0.1:8000/assets/ \
  -H "Content-Type: application/json" \
  -d '{"symbol":"PETR4","name":"Petrobras PN","asset_type":"stock","currency":"BRL"}' \
  | python3 -m json.tool
```

### Registrar entrada

```bash
curl -s -X POST http://127.0.0.1:8000/entries/ \
  -H "Content-Type: application/json" \
  -d '{"asset_id":"<uuid>","quantity":100,"unit_price":36.50}' \
  | python3 -m json.tool
```

### Consultar posições consolidadas

```bash
curl -s http://127.0.0.1:8000/wallet/positions/ | python3 -m json.tool
```

### Consultar resumo da carteira

```bash
curl -s http://127.0.0.1:8000/wallet/summary/ | python3 -m json.tool
```

## Limites do MVP

- **Sem persistência**: dados são perdidos ao reiniciar a API.
- **Sem autenticação**: qualquer cliente tem acesso a todos os endpoints.
- **Sem cotação externa**: o preço de referência atual é o `unit_price` da entrada mais recente do ativo.
- **Sem cálculo tributário**.
- **Sem integração com corretoras**.
- **Sem suporte a vendas**: entradas representam compras; cancelamento de lançamento remove a entrada, não registra venda.
- **Concorrência não garantida**: o armazenamento em memória não usa locks.

## Uso de IA generativa no desenvolvimento

Este projeto foi desenvolvido com assistência de dois modelos de IA generativa ao longo do ciclo:

- **Elicitação de requisitos**: OpenAI Codex — apoio na definição de escopo, backlog e estrutura inicial de prompts CO-STAR.
- **Geração assistida de código**: Claude (Anthropic) — cada incremento foi produzido a partir de um prompt estruturado registrado em `prompts/`.
- **Revisão e qualidade**: Claude — ajuste de padrões, isolamento de testes e contratos de resposta.
- **Documentação**: Claude — geração e revisão da documentação técnica.

Nenhum dos dois modelos **está presente em runtime** na aplicação. Não há chamadas a modelos de linguagem durante a execução da API.

Todos os prompts utilizados estão versionados em `prompts/` para transparência e reprodutibilidade.

## Próximos passos (fora do MVP)

- Persistência em banco de dados relacional.
- Autenticação e multi-usuário.
- Integração com cotações externas.
- Registro de vendas e cálculo de P&L realizado.
- Cálculo tributário.
- Recomendação assistida por IA (PortfolioAdvisor).
