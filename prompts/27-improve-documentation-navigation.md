← [README principal](../README.md) · [Índice de prompts](README.md)

# Prompt 27 - Melhorar navegação da documentação

## Metadados

- **Data:** 2026-05-03
- **Release alvo:** Release 5 - Qualidade e estabilização
- **Modelo utilizado:** Claude Sonnet 4.6

---

## Prompt (CO-STAR)

### C - Contexto
Documentação técnica do projeto existente, mas sem navegação entre artefatos — pasta `docs/` sem índice, arquitetura exposta apenas como `.mmd` bruto, pasta `prompts/` sem página inicial.

### O - Objetivo
Melhorar a navegabilidade e apresentação da documentação do projeto, sem alterar código.

### S - Estilo
Documentação clara, objetiva e amigável. Links internos úteis. Coerência com o MVP implementado.

### T - Tom
Profissional, simples e didático.

### A - Audiência
Professor avaliador, colegas de turma e desenvolvedores que acabam de abrir o repositório.

### R - Resposta esperada
Criar páginas índice para `docs/` e `prompts/`, adicionar página amigável de arquitetura e incluir links de navegação nos documentos existentes.

---

## Arquivos criados/alterados

| Arquivo | Ação |
|---|---|
| `README.md` | Alterado — tabela "Documentação do projeto" aponta para páginas índice em vez de diretórios brutos |
| `docs/README.md` | Criado — índice da documentação com ordem de leitura recomendada |
| `docs/arquitetura-componentes.md` | Criado — página amigável com introdução, explicação das camadas e diagrama Mermaid embutido |
| `docs/escopo-MVP.md` | Alterado — links de navegação no início e no final |
| `docs/requisitos.md` | Alterado — links de navegação no início e no final |
| `docs/backlog-releases.md` | Alterado — link de navegação no início |
| `prompts/README.md` | Criado — índice comentado de todos os 27 prompts com links e padrão CO-STAR explicado |
| `prompts/27-improve-documentation-navigation.md` | Criado — este arquivo |

## Melhorias de navegação

- README aponta para `docs/README.md` e `prompts/README.md` em vez de diretórios brutos.
- Toda página de `docs/` tem links `← README principal · Índice da documentação` no topo e no rodapé.
- `docs/arquitetura-componentes.md` embute o diagrama Mermaid com texto introdutório — o `.mmd` bruto é mantido como referência.
- `prompts/README.md` lista todos os 27 prompts em ordem com link para cada um e explica o padrão CO-STAR.
