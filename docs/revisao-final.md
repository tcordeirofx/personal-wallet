← [README principal](../README.md) · [Índice da documentação](README.md)

# Revisão Final — Personal Wallet API

## Visão geral da entrega

O projeto entrega uma micro API REST offline para controle básico de carteira de ativos de renda variável. Desenvolvida de forma incremental em cinco releases, a aplicação cobre cadastro e gestão de ativos, registro e cancelamento de entradas, consulta de posições consolidadas e resumo geral da carteira.

O desenvolvimento foi conduzido com assistência de IA generativa em todas as etapas: elicitação (OpenAI Codex) e implementação, revisão e documentação (Claude). Todos os prompts estão versionados em [`prompts/`](../prompts/README.md).

---

## Escopo implementado

Todos os itens do backlog das Releases 0 a 4 foram concluídos. A Release 5 (qualidade e estabilização) foi integralmente completada.

| Release | Itens | Status |
|---|---|---|
| 0 — Kickoff documental | 7 | Concluída |
| 1 — Estrutura base da API | 6 | Concluída |
| 2 — Gestão de ativos | 6 | Concluída |
| 3 — Entradas/Transações | 5 | Concluída |
| 4 — Consultas de carteira | 4 | Concluída |
| 5 — Qualidade e estabilização | 4 | Concluída |

Endpoints entregues: `GET /health`, CRUD completo de `/assets/`, CRUD parcial de `/entries/` (sem atualização) e `GET /wallet/positions/` e `GET /wallet/summary/`.

---

## Análise da qualidade da implementação

### Pontos positivos

- **Separação de responsabilidades**: routers lidam com HTTP, services com regras de negócio, repositories com persistência. Nenhuma regra de domínio está no router.
- **Contratos explícitos**: todos os schemas de entrada e saída são definidos com Pydantic, incluindo validações (`min_length`, `gt=0`, normalização uppercase).
- **Consistência entre entidades**: a regra de bloqueio de remoção de ativo com entradas associadas está implementada e testada.
- **Injeção de dependência controlada**: `app/dependencies.py` centraliza os singletons dos repositórios, garantindo que `AssetService` e `EntryService` compartilhem o mesmo estado em produção.

### Pontos de atenção técnicos

- **`float` para valores monetários**: os campos `quantity`, `unit_price`, `average_price` e derivados usam `float`. Em carteiras com muitas entradas, o acúmulo de erros de ponto flutuante pode produzir imprecisões nas casas decimais. A migração para `Decimal` resolveria isso.
- **`_service` como singleton de módulo**: a instância `_service` em cada router é compartilhada entre todas as requisições. O armazenamento em memória funciona porque o processo é único, mas esse padrão não escala para ambientes com múltiplos workers sem adaptação.
- **Thread safety ausente**: o `dict` interno dos repositórios não usa locks. Requisições simultâneas podem produzir estado inconsistente em ambientes com concorrência real.
- **`entry_repo=None` em `AssetService`**: o parâmetro opcional permite que testes instanciem o service sem a verificação de consistência. É uma decisão funcional, mas pode surpreender quem mantiver o código sem contexto.

---

## Análise da cobertura de testes

A suíte contém **56 testes** distribuídos em 6 arquivos:

| Arquivo | Testes | Cobertura |
|---|---|---|
| `test_health.py` | 2 | Status e corpo do endpoint /health |
| `test_assets.py` | 10 | CRUD completo de ativos |
| `test_asset_validations.py` | 6 | Unicidade de symbol, normalização uppercase |
| `test_entries.py` | 11 | CRUD de entradas e consistência com ativos |
| `test_wallet.py` | 14 | Cálculos de posição, summary e allocation |
| `test_edge_cases.py` | 13 | Campos obrigatórios vazios, valores inválidos, borda |

**Isolamento**: cada teste recebe instâncias frescas de repositório via `monkeypatch`, sem contaminação de estado entre testes.

**O que não está coberto**: não há testes de carga, concorrência ou comportamento sob reinicialização da API (todos esses cenários estão fora do escopo do MVP).

---

## Análise da documentação

A documentação foi produzida incrementalmente e revisada na Release 5.

| Artefato | Avaliação |
|---|---|
| `README.md` | Completo: instalação, execução, testes, endpoints, exemplos, limites, uso de IA |
| `docs/escopo-MVP.md` | Coerente com o implementado; limites explícitos |
| `docs/requisitos.md` | RF, RNF e regras de negócio documentados com IDs |
| `docs/arquitetura-componentes.md` | Diagrama Mermaid com explicação das camadas |
| `docs/backlog-releases.md` | Evolução completa do projeto com checkboxes |
| `prompts/README.md` | Índice dos 28 prompts com padrão CO-STAR explicado |

**Lacuna identificada**: nenhum método ou classe possui docstring. Os casos mais relevantes para documentação interna seriam:
- `WalletService.get_positions()` — a lógica de `last_unit_price` via `max(..., key=created_at)` não é óbvia.
- `AssetService.delete()` — o comportamento condicional com `entry_repo=None` merece explicação.
- `AssetRepository` / `EntryRepository` — a volatilidade dos dados ao reiniciar a API vale ser registrada em docstring de classe.

---

## Como a GenAI foi usada no processo

O desenvolvimento utilizou dois modelos em papéis distintos:

- **OpenAI Codex**: apoio na fase elicitativa — definição de escopo, backlog inicial e estrutura de prompts.
- **Claude (Anthropic)**: geração assistida de código em cada incremento, revisão de padrões, isolamento de testes e produção da documentação técnica.

Cada incremento foi conduzido por um prompt CO-STAR registrado em `prompts/`. O modelo nunca atuou de forma autônoma: cada saída foi revisada antes de ser integrada ao repositório.

**A IA não está presente em runtime.** A aplicação não faz chamadas a modelos de linguagem durante sua execução.

---

## Limitações conhecidas

| Limitação | Impacto | Mitigação futura |
|---|---|---|
| Dados em memória | Perdidos ao reiniciar a API | Adicionar persistência (SQLite, PostgreSQL) |
| `float` para valores monetários | Imprecisão em casas decimais | Migrar para `Decimal` |
| Sem autenticação | Qualquer cliente acessa todos os dados | Implementar OAuth2 ou API key |
| Sem concorrência segura | Possível estado inconsistente com múltiplos workers | Adicionar locks ou usar banco de dados com transações |
| Preço sem cotação externa | `last_unit_price` depende de entrada manual | Integrar com API de cotações |
| Sem registro de vendas | Entradas só representam compras | Modelar transações de venda separadamente |

---

## Riscos e pontos de atenção

- **Imprecisão monetária**: testes passam com `pytest.approx`, mas a imprecisão existe. Para uso financeiro real, `float` é inadequado.
- **Singleton sem isolamento em produção**: `_service = AssetService(...)` a nível de módulo funciona em processo único, mas não é adequado para deploy com múltiplos workers (Gunicorn, etc.) sem revisão da gestão de estado.
- **Sem validação de tipos de ativo**: `asset_type` aceita qualquer string não-vazia. Um `Enum` ou lista de valores permitidos tornaria o contrato mais robusto.
- **`entry_repo=None` como design decision implícita**: quem não conhecer o histórico do projeto pode remover o parâmetro sem perceber que isso desativa a verificação de consistência.

---

## Melhorias futuras

1. **Persistência**: migrar para SQLite (mínimo) ou PostgreSQL com SQLAlchemy.
2. **Autenticação**: adicionar autenticação por API key ou OAuth2.
3. **`Decimal` para valores financeiros**: substituir `float` em todos os campos monetários.
4. **Injeção de dependência com FastAPI `Depends`**: substituir o padrão `_service` de módulo por DI nativa do framework.
5. **`Enum` para `asset_type`**: restringir os tipos aceitos a valores conhecidos (ação, FII, ETF, etc.).
6. **Registro de vendas**: modelar transações de venda para permitir cálculo de P&L realizado.
7. **Integração com cotações externas**: substituir `last_unit_price` manual por preço de mercado.
8. **PortfolioAdvisor**: funcionalidade futura de recomendação assistida por IA, fora do escopo deste MVP.

---

## Conclusão

O MVP cumpre o escopo proposto. A implementação é coerente, testada e documentada em nível adequado para o contexto acadêmico e para demonstração do uso de GenAI no processo de desenvolvimento.

Os principais riscos técnicos — uso de `float` para valores monetários e ausência de thread safety — são aceitáveis no contexto offline e de processo único do MVP, mas devem ser endereçados antes de qualquer uso em produção.

O uso de IA generativa foi documentado, rastreável e revisado em cada etapa. O processo demonstra que é possível desenvolver software incrementalmente com assistência de modelos de linguagem sem abrir mão de qualidade, testes e documentação.

---

← [README principal](../README.md) · [Índice da documentação](README.md)
