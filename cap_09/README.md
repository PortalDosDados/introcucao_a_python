# Capítulo 9 ■ Arquivos

A manipulação de arquivos permite persistir dados entre execuções de programas, processar grandes volumes de texto, gerar relatórios em diferentes formatos (como texto simples, CSV e HTML) e interagir com o sistema operacional.

---

## 9.1 Abertura e Fechamento de Arquivos

Para abrir um arquivo em Python, utilizamos a função embutida `open()`:

```python
arquivo = open("dados.txt", "w", encoding="utf-8")
arquivo.write("Primeira linha\n")
arquivo.close()
```

### Modos de Abertura Comuns:
- `'r'`: Leitura (modo padrão). O arquivo deve existir.
- `'w'`: Escrita. Cria um novo arquivo ou sobrescreve o arquivo existente.
- `'a'`: Anexo (*append*). Adiciona conteúdo ao final do arquivo sem sobrescrevê-lo.
- `'r+'`: Leitura e escrita.
- `'b'`: Modo binário (usado junto a outros modos, ex.: `'rb'`, `'wb'`).

---

## 9.2 O Gerenciador de Contexto (`with`)

A instrução `with` garante que o arquivo seja fechado adequadamente após a conclusão do bloco, mesmo que ocorram exceções ou erros:

```python
with open("dados.txt", "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())
```

---

## 9.3 Métodos Principais de Leitura e Escrita

- `f.read()`: Lê todo o conteúdo do arquivo como uma única string.
- `f.readline()`: Lê uma linha por vez (incluindo o caractere `\n`).
- `f.readlines()`: Lê todas as linhas e retorna uma lista de strings.
- `f.write(texto)`: Escreve a string `texto` no arquivo.
- `f.writelines(lista)`: Escreve uma sequência de strings no arquivo.

---

## 9.4 Argumentos da Linha de Comando (`sys.argv`)

A lista `sys.argv` do módulo `sys` fornece acesso aos parâmetros passados na inicialização do programa via terminal:

```python
import sys

print(f"Nome do script: {sys.argv[0]}")
if len(sys.argv) > 1:
    print(f"Primeiro argumento: {sys.argv[1]}")
```

---

## 9.5 Navegação no Sistema de Arquivos (`os` e `os.path`)

- `os.path.exists(caminho)`: Verifica se o arquivo ou diretório existe.
- `os.path.isfile(caminho)`: Retorna `True` se o caminho for um arquivo.
- `os.path.isdir(caminho)`: Retorna `True` se o caminho for um diretório.
- `os.listdir(caminho)`: Lista o conteúdo de uma pasta.
- `os.path.join(pasta, arquivo)`: Concatena caminhos respeitando os separadores do sistema operacional.
- `os.walk(caminho)`: Percorre recursivamente uma árvore de diretórios.

---

## 9.6 Processamento de Dados Estruturados e Geração de HTML

O capítulo explora o desenvolvimento de miniaplicações, como cadastros em texto (agendas), leituras de arquivos CSV e geradores automáticos de páginas Web formatadas em HTML.
