# 00-overview.md - Visão Geral e Ciclo de Vida

## Escopo e Contexto
- **Objetivo**: Estudo e resolução dos exercícios do livro "Introdução à Programação com Python" (Nilo Coutinho) [README.md].
- **Natureza**: Repositório educacional com scripts autônomos por capítulo [OBSERVADO].

## Stack e Dependências
- **Linguagem**: Python 3 (versão de referência sugerida: 3.10+) [SUGESTÃO (confirmar)].
- **Sintaxe mínima observada**: Python 3.6+ devido ao uso de f-strings [cap_03/ex_3.12.py:13].
- **Gerenciador de Pacotes**: NÃO IDENTIFICADO [sem manifestos].
- **Dependências Externas**: NENHUMA [OBSERVADO]. Uso restrito à biblioteca padrão (`standard library`).

## Comandos Fundamentais
- **Instalação de Dependências**: NÃO IDENTIFICADO (apenas interpretador nativo).
- **Execução de Script**:
  ```bash
  python <pasta_capitulo>/<nome_arquivo>.py
  # Exemplo:
  python cap_03/ex_3.12.py
  ```
  [SUGESTÃO (confirmar)]
- **Validação Sintática Local**:
  ```bash
  python -m py_compile <pasta_capitulo>/<nome_arquivo>.py
  ```
  [SUGESTÃO (confirmar)]
- **Formatação de Código**: `black` (padrão de mercado para formatação opinativa PEP 8) [DIRETRIZ]:
  ```bash
  # Formatação automática:
  black <pasta_capitulo>/<nome_arquivo>.py
  # Verificação sem alteração:
  black --check <pasta_capitulo>/<nome_arquivo>.py
  ```
- **Lint / Análise Estática**: NÃO IDENTIFICADO no repositório.
- **Testes Automatizados**: NÃO IDENTIFICADO no repositório.

## Regras Operacionais para IA
- **SEMPRE** executar validação sintática (`py_compile`) após editar qualquer arquivo `.py`.
- **NUNCA** instalar ou introduzir pacotes externos (`pip install ...`) sem aprovação explícita.
- **NUNCA** criar arquivos de build, empacotamento ou dependências (`setup.py`, `pyproject.toml`) sem autorização.
- **PREFIRA** manter os scripts compatíveis com interpretador Python 3 padrão de linha de comando.
