# Personal Wallet API

API offline para controle simples de carteira de ativos de renda variável.

## Objetivo do projeto
Este repositório faz parte de um desafio acadêmico para demonstrar uso de GenAI no desenvolvimento de software de forma incremental, documentada, testável e versionada.

Nesta etapa inicial, o foco é estruturar o projeto com documentação de escopo, backlog, arquitetura mínima e padrão de prompts.

## Proposta do MVP
O MVP (offline, com armazenamento em memória) deve evoluir para permitir:
- cadastro, listagem, atualização e remoção de ativos;
- registro de entradas/transações da carteira;
- listagem de histórico de entradas;
- remoção/cancelamento de entrada;
- consulta de posições consolidadas;
- consulta de resumo geral da carteira.

## Fora do escopo do MVP
- cotação externa;
- integração com corretora;
- autenticação;
- banco de dados;
- cálculo tributário;
- recomendação financeira;
- uso de GenAI dentro da aplicação.

## Pré-requisitos

- Python 3.11 ou superior
- make

Validar o ambiente:

```bash
python3 --version
make --version
```

## Ambiente virtual

O projeto usa um virtual environment local em `.venv/`.
`make install` cria o ambiente automaticamente caso ele não exista e instala as dependências dentro dele:

```bash
make install
```

## Stack prevista
- Python
- FastAPI
- Pydantic
- Pytest
- Armazenamento em memória

## Status atual
- Projeto em fase de kickoff documental.
- Sem implementação de código da aplicação nesta etapa.
- Repositório preparado para evolução incremental nas próximas entregas.
