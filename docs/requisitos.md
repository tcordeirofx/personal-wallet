# Requisitos - Personal Wallet API

## Requisitos Funcionais

| ID | Descrição |
|---|---|
| RF01 | Cadastrar ativo com `symbol`, `name`, `asset_type` e `currency`. |
| RF02 | Listar todos os ativos cadastrados. |
| RF03 | Atualizar parcialmente um ativo existente. |
| RF04 | Remover ativo existente. |
| RF05 | Registrar entrada/transação com `asset_id`, `quantity` e `unit_price`. |
| RF06 | Listar histórico de entradas. |
| RF07 | Cancelar/remover entrada existente. |
| RF08 | Consultar posições consolidadas por ativo (`GET /wallet/positions/`). |
| RF09 | Consultar resumo geral da carteira (`GET /wallet/summary/`). |

## Requisitos Não Funcionais

| ID | Descrição |
|---|---|
| RNF01 | API offline, sem dependências de serviços externos. |
| RNF02 | Armazenamento em memória (sem banco de dados). |
| RNF03 | Execução local reproduzível via `make install` + `make run`. |
| RNF04 | Testes automatizados com Pytest, executáveis via `make test`. |
| RNF05 | Separação de responsabilidades em routers, services e repositories. |
| RNF06 | Contratos de entrada e saída explícitos via schemas Pydantic. |
| RNF07 | Documentação OpenAPI gerada automaticamente pelo FastAPI em `/docs`. |
| RNF08 | Sem credenciais ou dados sensíveis versionados no repositório. |
| RNF09 | Compatível com Python 3.11 ou superior. |

## Regras de Negócio

| ID | Descrição |
|---|---|
| RN01 | Ativo não pode ter `symbol` duplicado (unicidade case-insensitive pela normalização). |
| RN02 | `symbol` e `currency` são normalizados para uppercase no cadastro e na atualização. |
| RN03 | Entrada só pode ser registrada para ativo existente (`asset_id` válido). |
| RN04 | Não é permitido remover ativo que possui entradas associadas. |
| RN05 | Remoção de entrada representa cancelamento de lançamento, não venda de ativo. |
| RN06 | `quantity` e `unit_price` de uma entrada devem ser estritamente maiores que zero. |
| RN07 | Posição consolidada usa o `unit_price` da entrada mais recente como preço de referência atual (sem cotação externa). |
| RN08 | `average_price` é calculado como média ponderada pela quantidade das entradas do ativo. |
| RN09 | Campos obrigatórios de ativo (`symbol`, `name`, `asset_type`, `currency`) não podem ser strings vazias. |

## Fora de Escopo

- Cotação de preços em tempo real ou via API externa.
- Integração com corretoras.
- Autenticação e autorização.
- Persistência em banco de dados.
- Cálculo tributário.
- Recomendação financeira.
- Uso de GenAI em runtime na aplicação.
- Registro de vendas de ativos.
- Suporte a múltiplos usuários ou múltiplas carteiras.

## Critérios de Aceite

- Todos os endpoints dos RF respondem com status codes corretos.
- Regras de negócio retornam erros HTTP apropriados:
  - **409 Conflict** — conflito de domínio (symbol duplicado, ativo com entradas).
  - **404 Not Found** — recurso inexistente.
  - **422 Unprocessable Entity** — dados de entrada inválidos (validação Pydantic).
- `make test` passa com 56 ou mais testes.
- A API inicializa via `make run` em ambiente Python 3.11+.
- Documentação interativa acessível em `/docs`.
