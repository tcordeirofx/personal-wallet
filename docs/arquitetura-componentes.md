← [README principal](../README.md) · [Índice da documentação](README.md)

# Arquitetura — Personal Wallet API

## Visão geral

A aplicação segue uma arquitetura em camadas com separação clara de responsabilidades:

| Camada | Localização | Responsabilidade |
|---|---|---|
| **Routers** | `app/routers/` | Receber requisições HTTP, validar entrada e retornar resposta |
| **Services** | `app/services/` | Aplicar regras de negócio e orquestrar operações |
| **Repositories** | `app/repositories/` | Persistir e recuperar dados do armazenamento em memória |
| **Schemas** | `app/schemas/` | Definir contratos de entrada e saída via Pydantic |

O ponto de entrada da aplicação é `app/main.py`, que instancia o app FastAPI e registra os routers.

## Componentes principais

- **`AssetService`** — gerencia ativos, incluindo validações de domínio (unicidade de symbol, normalização de uppercase) e verificação de consistência antes de remoção.
- **`EntryService`** — gerencia entradas/transações, validando a existência do ativo referenciado.
- **`WalletService`** — calcula posições consolidadas e resumo da carteira a partir das entradas registradas.
- **`AssetRepository` / `EntryRepository`** — armazenamento em memória via `dict[UUID, T]`. Os dados são perdidos ao reiniciar a API.
- **`app/dependencies.py`** — instâncias singleton dos repositórios, compartilhadas entre services para garantir consistência de estado.

## Como ler o diagrama

- **Setas sólidas** (`-->`) indicam chamadas diretas entre componentes.
- **Setas tracejadas** (`-.->`) indicam dependências indiretas (consistência, geração de documentação, uso em testes).
- O bloco **Armazenamento em Memória** representa o estado em `dict` dentro de cada repositório.

## Diagrama de componentes

```mermaid
flowchart TD
    Client[Cliente HTTP]
    Swagger[Swagger UI / OpenAPI]

    subgraph API[FastAPI — app/main.py]
        RH[GET /health]
        R1[/assets router/]
        R2[/entries router/]
        R3[/wallet router/]
    end

    subgraph Services[Serviços]
        S1[AssetService]
        S2[EntryService]
        S3[WalletService]
    end

    subgraph Repositories[Repositórios]
        RepoA[AssetRepository]
        RepoE[EntryRepository]
    end

    subgraph Schemas[Schemas Pydantic]
        SC1[Asset / AssetCreate / AssetUpdate]
        SC2[WalletEntry / WalletEntryCreate]
        SC3[WalletPositionResponse / WalletSummaryResponse]
    end

    subgraph Tests[Testes — Pytest]
        T1[test_health]
        T2[test_assets / test_asset_validations]
        T3[test_entries]
        T4[test_wallet]
        T5[test_edge_cases]
    end

    Memory[(Armazenamento em Memória)]

    Client --> API
    Swagger -. gerado por .-> API

    R1 --> S1
    R2 --> S2
    R3 --> S3

    S1 --> RepoA
    S1 -.->|consistência| RepoE
    S2 --> RepoA
    S2 --> RepoE
    S3 --> RepoA
    S3 --> RepoE

    RepoA --> Memory
    RepoE --> Memory

    S1 --- SC1
    S2 --- SC2
    S3 --- SC3

    Tests -.->|TestClient| API
```

> O arquivo Mermaid bruto está disponível em [`arquitetura-componentes.mmd`](arquitetura-componentes.mmd).

---

← [README principal](../README.md) · [Índice da documentação](README.md)
