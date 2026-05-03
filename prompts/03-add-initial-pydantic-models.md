# Prompt 03 - Definir modelos Pydantic iniciais

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 1 - Estrutura base da API
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Você é o agente de desenvolvimento do projeto Personal Wallet API.

O projeto já possui uma aplicação FastAPI mínima, requirements.txt, Makefile, README com pré-requisitos e documentação inicial.

Produto:
Personal Wallet API é uma micro API offline para controle simples de uma carteira de ativos de renda variável.

O MVP trabalha com ativos, entradas/transações, posições consolidadas e resumo da carteira.

### O - Objetivo
Definir apenas os modelos/schemas Pydantic iniciais para ativo e entrada.

### S - Estilo
- Código simples, tipado e legível.
- Usar Pydantic para contratos de entrada e saída.
- Não implementar lógica de negócio nesta etapa.
- Não criar endpoints nesta etapa.

### T - Tom
- Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão os contratos da API.

### R - Resposta esperada
Schemas Asset, AssetCreate, AssetUpdate, WalletEntry, WalletEntryCreate com validações mínimas.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/schemas/__init__.py` | Criado — re-exporta todos os schemas públicos |
| `app/schemas/asset.py` | Criado — Asset, AssetCreate, AssetUpdate |
| `app/schemas/entry.py` | Criado — WalletEntry, WalletEntryCreate |
| `prompts/03-add-initial-pydantic-models.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox do item desta etapa marcado como concluído |

## Decisões técnicas

- **Herança entre schemas**: `Asset` herda de `AssetCreate` e `WalletEntry` herda de `WalletEntryCreate`, evitando repetição de campos.
- **`UUID` para ids**: mais adequado que `int` sequencial para uma API sem banco de dados real; o repositório em memória gerará os UUIDs.
- **`float` para quantity e unit_price**: suficiente para o MVP; pode migrar para `Decimal` em releases futuras se precisão decimal for requisito.
- **`str | None`** em `AssetUpdate`: sintaxe union nativa do Python 3.10+, compatível com Pydantic v2 e FastAPI >= 0.111.
- **`Field(min_length=1)`** em vez de `@field_validator`: validação declarativa mais simples para a restrição de string não-vazia.
- **`created_at` apenas em `WalletEntry`**: será preenchido pelo repositório no momento da criação, não exposto no schema de entrada.
