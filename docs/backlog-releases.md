# Backlog e Releases - Personal Wallet API

> Formato com checkboxes para acompanhamento incremental.

## Release 0 - Kickoff documental
- [x] Definir visão inicial do projeto no README.
- [x] Documentar escopo do MVP (objetivo, funcionalidades, fora de escopo, premissas e critérios).
- [x] Criar backlog faseado de evolução.
- [x] Registrar arquitetura mínima em Mermaid.
- [x] Criar template de prompt CO-STAR.
- [x] Registrar prompt de kickoff.
- [x] Ajustar .gitignore inicial para projeto Python/FastAPI.

## Release 1 - Estrutura base da API
- [x] Criar estrutura inicial da aplicação FastAPI.
- [ ] Definir modelos Pydantic iniciais (ativo e entrada).
- [ ] Organizar camadas (routers, services, repositories).
- [ ] Implementar armazenamento em memória para MVP.
- [ ] Criar endpoint de health check.

## Release 2 - Gestão de ativos
- [ ] Implementar cadastro de ativo.
- [ ] Implementar listagem de ativos.
- [ ] Implementar atualização de ativo.
- [ ] Implementar remoção de ativo.
- [ ] Adicionar validações de domínio básicas para ativo.

## Release 3 - Entradas/Transações
- [ ] Implementar registro de entrada.
- [ ] Implementar listagem de histórico de entradas.
- [ ] Implementar remoção/cancelamento de entrada.
- [ ] Garantir consistência mínima entre ativo e entradas.

## Release 4 - Consultas de carteira
- [ ] Implementar consulta de posições consolidadas.
- [ ] Implementar resumo geral da carteira.
- [ ] Revisar contratos de resposta dos endpoints de consulta.

## Release 5 - Qualidade e estabilização
- [ ] Criar suíte inicial de testes com Pytest.
- [ ] Cobrir fluxos principais e cenários de erro.
- [ ] Revisar documentação técnica.
- [ ] Preparar checklist de entrega final do desafio.
