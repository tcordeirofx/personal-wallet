# Prompt 04 - Organizar camadas da aplicação

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 1 - Estrutura base da API
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Projeto Personal Wallet API com FastAPI mínima, schemas Pydantic e documentação inicial.
A arquitetura planejada separa responsabilidades em routers, services, repositories e schemas.

### O - Objetivo
Organizar a estrutura de camadas da aplicação, sem implementar lógica de negócio ainda.

### S - Estilo
Estrutura simples e incremental. Separar responsabilidades por diretórios. Sem código complexo.

### T - Tom
Explicações curtas e técnicas.

### A - Audiência
Professor avaliador e desenvolvedores que revisarão a organização incremental do projeto.

### R - Resposta esperada
Criar os pacotes routers, services e repositories com stubs mínimos prontos para evolução.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `app/routers/__init__.py` | Criado — re-exporta os três routers |
| `app/routers/assets.py` | Criado — APIRouter vazio com prefix e tag |
| `app/routers/entries.py` | Criado — APIRouter vazio com prefix e tag |
| `app/routers/wallet.py` | Criado — APIRouter vazio com prefix e tag |
| `app/services/__init__.py` | Criado — re-exporta WalletService |
| `app/services/wallet_service.py` | Criado — classe vazia |
| `app/repositories/__init__.py` | Criado — re-exporta MemoryRepository |
| `app/repositories/memory_repository.py` | Criado — classe vazia |
| `prompts/04-organize-application-layers.md` | Criado — este arquivo |
| `docs/backlog-releases.md` | Alterado — checkbox desta etapa marcado como concluído |

## Decisões técnicas

- **`APIRouter` com `prefix` e `tags`** nos stubs: evita ter que redigitar esses metadados quando os endpoints forem adicionados; os valores refletem o domínio de cada router.
- **`WalletService` como classe única**: o service centraliza as regras de negócio da carteira; será decomposto se a complexidade exigir.
- **`MemoryRepository` como classe única**: encapsula todo o armazenamento em memória; separar por entidade seria prematuro neste ponto.
- **Re-exportações nos `__init__.py`**: permitem `from app.routers import assets_router` nos pontos de montagem, sem expor a estrutura interna de arquivos.
