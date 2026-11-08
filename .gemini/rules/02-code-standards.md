# 02-code-standards.md - Padrões de Código

## Cabeçalho e Documentação
- **SEMPRE** iniciar o arquivo com o enunciado do exercício em docstring com aspas triplas `''' ... '''` [cap_03/ex_3.12.py:1-8, cap_04/ex_4.10.py:1-8].
- **SEMPRE** incluir comentários explicativos em operações não triviais e regras de cálculo [cap_04/ex_4.10.py:10,35,46].

## Nomenclatura e Estilo
- **SEMPRE** utilizar `snake_case` em português para variáveis e funções [cap_03/ex_3.12.py:10-12].
- **SEMPRE** usar identificadores exclusivamente em caracteres ASCII sem acentos (`bonus`, `salario`) [DIRETRIZ].
  - Desvio a evitar: identificador acentuado `bônus` [cap_03/main.py:21].
- **NUNCA** utilizar nomes crípticos ou abreviações não consagradas (ex.: substituir `tp_inst` por `tipo_instalacao`) [cap_04/ex_4.10.py:37].

## Entrada, Saída e Tipagem
- **SEMPRE** utilizar `input()` com prompt claro em português para entrada interativa [cap_03/ex_3.12.py:10-11].
- **SEMPRE** realizar coerção explícita de tipos na entrada de dados (`int(...)`, `float(...)`) [cap_03/ex_3.12.py:10].
- **SEMPRE** utilizar *f-strings* para saída formatada (`print(f'... {valor:.2f}')`) [cap_03/ex_3.12.py:13].
- **PREFIRA** formatar valores monetários e decimais com duas casas (`:.2f}`) [cap_03/ex_3.12.py:13, cap_04/ex_4.10.py:56].

## Progressão Didática (Restrição Crítica)
- **SEMPRE** limitar as construções de linguagem ao conteúdo ensinado até o capítulo do arquivo [README.md:5-54]:
  - `cap_01` e `cap_02`: Operações aritméticas e variáveis básicas.
  - `cap_03`: Tipos primitivos, `input()`, conversões e operadores relacionais/lógicos.
  - `cap_04`: Estruturas condicionais (`if`, `elif`, `else`).
  - `cap_05`: Estrutura de repetição `while` (evitar `for` e funções até os capítulos específicos).
  - `cap_06`: Listas e manipulação de coleções.
  - `cap_08`: Definição de funções (`def`).
  - `cap_10`: Classes e objetos.
- **NUNCA** antecipar conceitos complexos ou recursos avançados que ultrapassem o capítulo correspondente.
