← [Voltar ao README principal](../README.md)

# Prompts — Personal Wallet API

Esta pasta contém todos os prompts utilizados no desenvolvimento do projeto, versionados como evidência do uso de IA generativa no processo.

## Por que os prompts estão aqui?

O projeto foi desenvolvido com assistência de OpenAI Codex (fase elicitativa) e Claude (geração de código, revisão e documentação). Versionar os prompts garante:

- **Transparência** — qualquer pessoa pode reproduzir ou auditar as decisões tomadas.
- **Rastreabilidade** — cada incremento do código tem um prompt correspondente.
- **Aprendizado** — os prompts documentam como a IA foi direcionada em cada etapa.

## Padrão utilizado: CO-STAR

Todos os prompts seguem o padrão **CO-STAR**:

| Componente | Descrição |
|---|---|
| **C** — Contexto | Estado atual do projeto e informações relevantes |
| **O** — Objetivo | O que deve ser feito nesta etapa |
| **S** — Estilo | Como o código ou texto deve ser escrito |
| **T** — Tom | Nível de linguagem e abordagem |
| **A** — Audiência | Para quem o resultado é destinado |
| **R** — Resposta esperada | O que deve ser entregue ao final |

O template base está em [`00-template-costar.md`](00-template-costar.md).

## Índice de prompts

| # | Arquivo | Etapa |
|---|---|---|
| 00 | [00-template-costar.md](00-template-costar.md) | Template CO-STAR base |
| 01 | [01-kickoff.md](01-kickoff.md) | Kickoff documental do projeto |
| 02 | [02-create-fastapi-structure.md](02-create-fastapi-structure.md) | Estrutura inicial da aplicação FastAPI |
| 03 | [03-add-initial-pydantic-models.md](03-add-initial-pydantic-models.md) | Schemas Pydantic para ativo e entrada |
| 04 | [04-organize-application-layers.md](04-organize-application-layers.md) | Organização das camadas (routers, services, repositories) |
| 05 | [05-add-in-memory-repositories.md](05-add-in-memory-repositories.md) | Armazenamento em memória para ativos e entradas |
| 06 | [06-add-health-check-endpoint.md](06-add-health-check-endpoint.md) | Endpoint GET /health |
| 07 | [07-add-health-check-test.md](07-add-health-check-test.md) | Teste automatizado para /health |
| 08 | [08-add-asset-create-endpoint.md](08-add-asset-create-endpoint.md) | POST /assets/ — cadastro de ativo |
| 09 | [09-add-asset-list-endpoint.md](09-add-asset-list-endpoint.md) | GET /assets/ — listagem de ativos |
| 10 | [10-add-asset-update-endpoint.md](10-add-asset-update-endpoint.md) | PUT /assets/{id}/ — atualização de ativo |
| 11 | [11-add-asset-delete-endpoint.md](11-add-asset-delete-endpoint.md) | DELETE /assets/{id}/ — remoção de ativo |
| 12 | [12-add-asset-domain-validations.md](12-add-asset-domain-validations.md) | Validações de domínio (unicidade, uppercase) |
| 13 | [13-add-asset-domain-validation-tests.md](13-add-asset-domain-validation-tests.md) | Testes para validações de domínio |
| 14 | [14-add-asset-management-tests.md](14-add-asset-management-tests.md) | Testes de CRUD de ativos |
| 15 | [15-add-entry-create-endpoint.md](15-add-entry-create-endpoint.md) | POST /entries/ — registro de entrada |
| 16 | [16-add-entry-list-endpoint.md](16-add-entry-list-endpoint.md) | GET /entries/ — histórico de entradas |
| 17 | [17-add-entry-delete-endpoint.md](17-add-entry-delete-endpoint.md) | DELETE /entries/{id}/ — cancelamento de entrada |
| 18 | [18-add-asset-entry-consistency.md](18-add-asset-entry-consistency.md) | Consistência entre ativos e entradas |
| 19 | [19-add-entry-management-tests.md](19-add-entry-management-tests.md) | Testes de entradas e consistência |
| 20 | [20-add-wallet-positions-endpoint.md](20-add-wallet-positions-endpoint.md) | GET /wallet/positions/ — posições consolidadas |
| 21 | [21-add-wallet-summary-endpoint.md](21-add-wallet-summary-endpoint.md) | GET /wallet/summary/ — resumo da carteira |
| 22 | [22-review-wallet-response-contracts.md](22-review-wallet-response-contracts.md) | Revisão dos contratos de resposta da carteira |
| 23 | [23-add-wallet-query-tests.md](23-add-wallet-query-tests.md) | Testes para consultas de carteira |
| 24 | [24-review-pytest-suite.md](24-review-pytest-suite.md) | Revisão da suíte de testes |
| 25 | [25-add-edge-case-tests.md](25-add-edge-case-tests.md) | Testes de cenários de erro e borda |
| 26 | [26-review-technical-documentation.md](26-review-technical-documentation.md) | Revisão da documentação técnica |
| 27 | [27-improve-documentation-navigation.md](27-improve-documentation-navigation.md) | Navegação entre artefatos de documentação |

## Como ler os prompts

Cada arquivo registra o prompt enviado ao modelo, os arquivos criados ou alterados e as decisões técnicas tomadas. A leitura em ordem cronológica mostra a evolução completa do projeto, do kickoff ao estado final.
