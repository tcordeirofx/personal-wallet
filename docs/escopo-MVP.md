← [README principal](../README.md) · [Índice da documentação](README.md)

# Escopo do MVP - Personal Wallet API

## Objetivo

Micro API offline para controle básico de carteira de ativos de renda variável, com foco em operações essenciais e sem integrações externas.

## Funcionalidades implementadas

### 1. Ativos

- Cadastrar ativo (`POST /assets/`).
- Listar ativos (`GET /assets/`).
- Atualizar ativo parcialmente (`PUT /assets/{asset_id}/`).
- Remover ativo (`DELETE /assets/{asset_id}/`).
- Validações: symbol único (case-insensitive), normalização de symbol e currency para uppercase.

### 2. Entradas/Transações

- Registrar entrada (`POST /entries/`).
- Listar histórico de entradas (`GET /entries/`).
- Cancelar/remover entrada (`DELETE /entries/{entry_id}/`).
- Consistência: entrada só pode ser criada para ativo existente; ativo com entradas não pode ser removido.

### 3. Consultas de carteira

- Posições consolidadas por ativo (`GET /wallet/positions/`).
- Resumo geral da carteira (`GET /wallet/summary/`).
- Cálculo baseado nas entradas registradas; preço de referência atual = `unit_price` da última entrada.

## Fora de escopo

- Qualquer integração online (cotações em tempo real, APIs externas).
- Integração com corretoras.
- Autenticação/autorização.
- Persistência em banco de dados.
- Cálculo tributário.
- Recomendação financeira.
- Uso de GenAI dentro da aplicação em runtime.
- Registro de vendas de ativos.

## Premissas

- MVP opera **offline**.
- Armazenamento é **em memória** — dados são perdidos ao reiniciar a API.
- API construída com FastAPI e contratos definidos com Pydantic.
- Testes automatizados com Pytest, cobrindo fluxos principais, validações e cenários de borda.

## Critérios de aceite do escopo

- Todas as funcionalidades listadas estão implementadas e testadas.
- Limites de escopo explicitamente registrados e respeitados.
- Operação offline garantida — sem chamadas a serviços externos.
- `make test` passa; `make run` inicializa a API.
- Documentação interativa disponível em `/docs`.

---

← [README principal](../README.md) · [Índice da documentação](README.md)
