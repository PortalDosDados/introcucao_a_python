# Roadmap de Desenvolvimento: Capítulos e Exercícios

Este documento orienta a estratégia de desenvolvimento, geração e controle de qualidade dos capítulos e exercícios do livro **"Introdução à Programação com Python"** (Nilo Ney Coutinho Menezes), assegurando a aderência às diretrizes de governança estabelecidas em [.gemini/rules/](.gemini/rules/).

---

## 1. Visão Geral e Status Atual

| Capítulo | Tema | Status | Exercícios Previstos |
| :--- | :--- | :---: | :---: |
| **Capítulo 01** | Motivação | Concluído | Scripts introdutórios |
| **Capítulo 02** | Preparando o Ambiente | Concluído | Cálculos e primeiras expressões |
| **Capítulo 03** | Variáveis e Entrada de Dados | Concluído | `ex_3.01` a `ex_3.15` |
| **Capítulo 04** | Condições | Concluído | `ex_4.01` a `ex_4.10` |
| **Capítulo 05** | Repetições | **Concluído** | `ex_5.1` a `ex_5.27` |
| **Capítulo 06** | Listas, Dicionários, Tuplas e Conjuntos | **Pendente** | `ex_6.01` a `ex_6.20` |
| **Capítulo 07** | Trabalhando com Strings | **Pendente** | `ex_7.01` a `ex_7.10` |
| **Capítulo 08** | Funções | **Pendente** | `ex_8.01` a `ex_8.15` |
| **Capítulo 09** | Arquivos | **Pendente** | `ex_9.01` a `ex_9.36` |
| **Capítulo 10** | Classes e Objetos | **Pendente** | `ex_10.01` a `ex_10.12` |
| **Capítulo 11** | Banco de Dados (SQLite) | **Pendente** | `ex_11.01` a `ex_11.06` |

---

## 2. Ciclo de Vida Padrão por Capítulo

Cada capítulo seguirá estritamente as quatro etapas abaixo antes do avanço para o próximo:

```
[1. Estruturação] ──► [2. Implementação] ──► [3. Validação] ──► [4. Versionamento]
  - cap_XX/            - ex_X.YY.py           - py_compile        - Usuário: `commit`
  - README.md          - Enunciado no topo    - black .           - Push origin/main
```

1. **Estruturação (`cap_XX/`)**:
   - Criação do diretório do capítulo.
   - Criação do `README.md` com a teoria essencial, síntese das listagens e conceitos apresentados pelo autor.

2. **Implementação Didática**:
   - Criação de cada script no formato `ex_X.YY.py`.
   - Inclusão do enunciado integral do exercício em docstring tripla `""" ... """` no topo do arquivo.
   - **Progressão Didática Rigorosa**: Utilizar exclusivamente estruturas introduzidas até aquele capítulo (ex.: nunca usar funções ou listas no Capítulo 5).
   - Nomes de identificadores em `snake_case` e exclusivamente caracteres ASCII (sem acentos ou cedilha).

3. **Validação e Qualidade**:
   - Compilação sintática de todos os arquivos: `python -m py_compile cap_XX/*.py`.
   - Formatação segundo a PEP 8 e padronização com Black: `black cap_XX/`.

4. **Revisão e Versionamento**:
   - Apresentação do resumo de alterações ao usuário.
   - Execução do atalho `commit` para inclusão e envio para o GitHub.

---

## 3. Detalhamento das Fases

### Fase 1: Capítulo 05 — Repetições
- **Foco Didático**: Laço `while`, contadores, acumuladores, interrupções com `break`, laços aninhados e controle de fluxo booleano.
- **Restrições**: Proibido o uso de listas, tuplas, dicionários, funções customizadas (`def`) ou POO.
- **Entregáveis**:
  - `cap_05/README.md`
  - Exercícios `ex_5.1.py` até `ex_5.27.py`

### Fase 2: Capítulo 06 — Listas, Dicionários, Tuplas e Conjuntos
- **Foco Didático**: Listas homogêneas e heterogêneas, índices, fatiamento, `append`, `pop`, laço `for`, filas (FIFO), pilhas (LIFO), pesquisa sequencial, ordenação por bolha (bubble sort), dicionários e conjuntos.
- **Restrições**: Proibido o uso de funções customizadas (`def`) ou bibliotecas externas.
- **Entregáveis**:
  - `cap_06/README.md`
  - Exercícios `ex_6.1.py` até `ex_6.20.py`

### Fase 3: Capítulo 07 — Trabalhando com Strings
- **Foco Didático**: Fatiamento de strings, métodos de busca e substituição (`find`, `replace`, `split`, `join`), validação de caracteres, formatação posicional e o projeto prático do Jogo da Forca.
- **Restrições**: Sem uso de orientação a objetos ou módulos avançados.
- **Entregáveis**:
  - `cap_07/README.md`
  - Exercícios `ex_7.1.py` até `ex_7.10.py`

### Fase 4: Capítulo 08 — Funções
- **Foco Didático**: Declaração `def`, retorno de valores (`return`), variáveis locais vs globais, parâmetros posicionais e opcionais, empacotamento/desempacotamento (`*args`, `**kwargs`), recursão e expressões lambda.
- **Entregáveis**:
  - `cap_08/README.md`
  - Exercícios `ex_8.1.py` até `ex_8.15.py`

### Fase 5: Capítulo 09 — Arquivos
- **Foco Didático**: Manipulação de arquivos texto (`open`, `with`, `read`, `readline`, `write`), geração de relatórios, processamento de logs, geração de páginas HTML e parâmetros de linha de comando (`sys.argv`).
- **Entregáveis**:
  - `cap_09/README.md`
  - Exercícios `ex_9.1.py` até `ex_9.36.py`

### Fase 6: Capítulo 10 — Classes e Objetos
- **Foco Didático**: Programação Orientada a Objetos (POO), modelagem de classes, atributos de instância, construtor `__init__`, métodos, herança, polimorfismo e composição.
- **Entregáveis**:
  - `cap_10/README.md`
  - Exercícios `ex_10.1.py` até `ex_10.12.py`

### Fase 7: Capítulo 11 — Banco de Dados
- **Foco Didático**: Introdução a SQL, módulo `sqlite3`, criação de tabelas, inserção, consulta, atualização, deleção, uso de cursores e prevenção de injeção SQL com parâmetros nomeados/posicionais.
- **Entregáveis**:
  - `cap_11/README.md`
  - Exercícios `ex_11.1.py` até `ex_11.6.py`

---

## 4. Governança e Regras de Apoio

- [00-overview.md](.gemini/rules/00-overview.md): Visão geral do repositório e stack.
- [01-architecture.md](.gemini/rules/01-architecture.md): Organização em `cap_XX/` e isolamento.
- [02-code-standards.md](.gemini/rules/02-code-standards.md): Padrões de código e convenções Python.
- [03-testing-and-quality.md](.gemini/rules/03-testing-and-quality.md): Checklist de testes e formatação com Black.
