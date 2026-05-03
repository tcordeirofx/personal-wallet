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
- [x] Definir modelos Pydantic iniciais (ativo e entrada).
- [x] Organizar camadas (routers, services, repositories).
- [x] Implementar armazenamento em memória para MVP.
- [x] Criar endpoint de health check.
- [x] Criar teste automatizado para health check.

## Release 2 - Gestão de ativos
- [x] Implementar cadastro de ativo.
- [x] Implementar listagem de ativos.
- [x] Implementar atualização de ativo.
- [x] Implementar remoção de ativo.
- [x] Adicionar validações de domínio básicas para ativo.
- [x] Criar testes automatizados para gestão de ativos.

## Release 3 - Entradas/Transações
- [x] Implementar registro de entrada.
- [x] Implementar listagem de histórico de entradas.
- [ ] Implementar remoção/cancelamento de entrada.
- [ ] Garantir consistência mínima entre ativo e entradas.
- [ ] Criar testes automatizados para entradas/transações.

## Release 4 - Consultas de carteira
- [ ] Implementar consulta de posições consolidadas.
- [ ] Implementar resumo geral da carteira.
- [ ] Revisar contratos de resposta dos endpoints de consulta.
- [ ] Criar testes automatizados para consultas de carteira.

## Release 5 - Qualidade e estabilização
- [ ] Revisar suíte de testes com Pytest.
- [ ] Cobrir cenários adicionais de erro e borda.
- [ ] Revisar documentação técnica.
- [ ] Preparar checklist de entrega final do desafio.