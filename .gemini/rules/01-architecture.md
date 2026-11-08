# 01-architecture.md - Arquitetura e Organização

## Estrutura de Diretórios
- `/`: Raiz do repositório contendo `README.md`, `.gitignore`, `.gitattributes`.
- `/cap_XX/`: Diretório correspondente a cada capítulo do livro (ex.: `cap_01`, `cap_02`, `cap_03`, `cap_04`) [OBSERVADO].
  - Previsto no índice do livro até `cap_12` [README.md:5-54].
- `/cap_XX/README.md`: Resumo teórico e anotações dos tópicos do capítulo [OBSERVADO].
- `/cap_XX/main.py`: Código demonstrativo, anotações de estudo e exemplos interativos (`#%%`) [cap_02/main.py:1,12].
- `/cap_XX/ex_<cap>.<num>.py`: Solução isolada do respectivo exercício [OBSERVADO: `ex_3.12.py`, `ex_4.10.py`].

## Fronteiras e Acoplamento
- **Isolamento de Scripts**: Cada exercício é um script autônomo e independente [OBSERVADO].
- **SEMPRE** manter cada script autocontido, sem dependência cruzada entre arquivos de exercícios ou entre capítulos.
- **NUNCA** importar funções ou variáveis entre arquivos de exercícios (ex.: `from ex_4.2 import ...`).
- **NUNCA** alterar arquivos fora do capítulo da tarefa solicitada.

## Convenções Estruturais
- **SEMPRE** utilizar caixa baixa e padding duplo para nomes de diretórios: `cap_01/` a `cap_12/` [OBSERVADO].
- **SEMPRE** nomear notas conceituais do capítulo como `README.md` com caixa alta correta [DIRETRIZ].
  - Normalizar desvio observado `cap_03/ReADME.md` para `cap_03/README.md`.
- **PREFIRA** padronizar a nomenclatura de exercícios no formato `ex_<cap>.<num>.py` (ex.: `ex_3.12.py`) [OBSERVADO].
  - Evitar variações divergentes como `ex_02.py` sem prefixo do capítulo [cap_03/ex_02.py].
