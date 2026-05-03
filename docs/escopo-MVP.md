# Escopo do MVP - Personal Wallet API

## Objetivo
Definir uma micro API offline para controle básico de carteira de ativos de renda variável, com foco em operações essenciais e sem integrações externas.

## Funcionalidades do MVP
1. **Ativos**
   - Cadastrar ativo.
   - Listar ativos.
   - Atualizar ativo.
   - Remover ativo.

2. **Entradas/Transações**
   - Registrar entrada de carteira.
   - Listar histórico de entradas.
   - Remover/cancelar entrada.

3. **Consultas de carteira**
   - Consultar posições consolidadas.
   - Consultar resumo geral da carteira.

## Fora de escopo
- Qualquer integração online (ex.: cotações em tempo real).
- Integração com corretoras.
- Autenticação/autorização.
- Persistência em banco de dados.
- Cálculo tributário.
- Recomendação financeira.
- Uso de GenAI dentro da aplicação em runtime.

## Premissas
- MVP operará **offline**.
- Armazenamento será **em memória**.
- API será construída com FastAPI e modelos com Pydantic.
- A cobertura de testes será adicionada em etapas futuras.

## Critérios de aceite do escopo
- Escopo funcional do MVP documentado e alinhado com objetivo inicial.
- Limites de escopo (não objetivos) explicitamente registrados.
- Premissa de operação offline claramente definida.
- Documento apto para orientar backlog e implementação incremental.
