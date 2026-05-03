# Prompt 05 - Implementar armazenamento em memória

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 1 - Estrutura base da API
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com FastAPI, schemas Pydantic e camadas organizadas.
O MVP usa armazenamento em memória sem banco de dados.

### O - Objetivo
Implementar apenas o armazenamento em memória para ativos e entradas/transações.

### S - Estilo
Código simples, tipado e legível. Repositórios fáceis de entender e testar.

### T - Tom
Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a separação de responsabilidades.

### R - Resposta esperada
`AssetRepository` e `EntryRepository` em memória com operações internas básicas.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/repositories/memory_repository.py` | Alterado — implementa `AssetRepository` e `EntryRepository` |
| `app/repositories/__init__.py` | Alterado — re-exporta as duas classes (necessário após renomear `MemoryRepository`) |
| `prompts/05-add-in-memory-repositories.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Decisões técnicas

- **Dois repositórios distintos** (`AssetRepository`, `EntryRepository`): separação de responsabilidade mais clara do que um único `MemoryRepository` contendo ambos.
- **`dict[UUID, T]` como store**: lookup e delete O(1) por chave; mais adequado que lista para operações por id.
- **`uuid4()` gerado internamente**: o caller não precisa conhecer nem gerar IDs — mesma convenção de banco de dados com PK autogerada.
- **`model_copy(update=...)`**: API nativa do Pydantic v2 para atualização parcial imutável; evita manipulação manual de dicionário.
- **`data.model_dump(exclude_none=True)` no `update`**: ignora campos não fornecidos em `AssetUpdate`, preservando os valores atuais.
- **`datetime.now(timezone.utc)` em `EntryRepository.create`**: timestamp UTC explícito; evita `datetime.utcnow()` que retorna naive datetime (deprecated no Python 3.12).
- **`list_by_asset`**: operação auxiliar adicionada em `EntryRepository` para suportar as queries de posição/resumo da Release 4 sem retrabalho.
- **`__init__.py` atualizado**: ajuste mínimo necessário; `MemoryRepository` substituída por `AssetRepository` e `EntryRepository`.
