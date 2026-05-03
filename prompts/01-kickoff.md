# Prompt 01 - Kickoff documental

## C - Contexto
Você é o agente de desenvolvimento do projeto Personal Wallet API.

Este projeto faz parte de um desafio acadêmico cujo objetivo é demonstrar o uso de GenAI no desenvolvimento de software de forma incremental, documentada, testável e versionada.

O repositório está no início. Antes de implementar código, precisamos criar os artefatos iniciais de elicitação, escopo, backlog, arquitetura mínima e padrão de prompts.

Produto:
Personal Wallet API é uma micro API offline para controle simples de uma carteira de ativos de renda variável.

O MVP deve permitir, futuramente:
- cadastrar, listar, atualizar e remover ativos;
- registrar entradas/transações de carteira;
- listar histórico de entradas;
- remover/cancelar uma entrada;
- consultar posições consolidadas da carteira;
- consultar resumo geral da carteira.

Fora do escopo do MVP:
- cotação externa;
- integração com corretora;
- autenticação;
- banco de dados;
- cálculo tributário;
- recomendação financeira;
- uso de GenAI dentro da aplicação.

Stack planejada:
- Python
- FastAPI
- Pydantic
- Pytest
- armazenamento em memória

## O - Objetivo
Criar apenas a documentação inicial e os arquivos de organização do projeto.

## S - Estilo
- Documentação clara, objetiva e técnica.
- Sem linguagem excessivamente acadêmica.
- Estrutura simples e fácil de manter.
- Não implementar código da aplicação nesta etapa.
- Não antecipar decisões técnicas que ainda serão tratadas em etapas futuras.

## T - Tom
- Direto, profissional e didático.
- Explicar decisões de forma curta.
- Evitar linguagem promocional ou genérica.

## A - Audiência
Professor avaliador, desenvolvedor responsável pelo projeto e qualquer pessoa que precise reproduzir a entrega.

## R - Resposta esperada
Criar ou alterar apenas os seguintes arquivos:
- README.md
- docs/escopo-MVP.md
- docs/backlog-releases.md
- docs/arquitetura-componentes.mmd
- prompts/00-template-costar.md
- prompts/01-kickoff.md
- .gitignore
