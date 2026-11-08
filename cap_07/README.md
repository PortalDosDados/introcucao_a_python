# Capítulo 7 ■ Trabalhando com Strings

Strings em Python são sequências imutáveis de caracteres. O Python disponibiliza um vasto conjunto de métodos para manipulação, busca, formatação e transformação textual.

---

## 7.1 Strings como sequências e fatiamento

Podemos acessar caracteres individuais por índice ou obter fatias (*slices*):

```python
s = "Python"
print(s[0])     # 'P'
print(s[-1])    # 'n'
print(s[1:4])   # 'yth'
print(s[::-1])  # Inverte a string: 'nohtyP'
```

---

## 7.2 Métodos de pesquisa e contagem

- `s.find(sub)`: Retorna o índice da primeira ocorrência de `sub` ou `-1` se não for encontrado.
- `s.rfind(sub)`: Retorna o índice da última ocorrência de `sub`.
- `s.count(sub)`: Conta quantas vezes a substring `sub` ocorre em `s`.
- `s.startswith(prefixo)` e `s.endswith(sufixo)`: Verificam início e fim da string (retornam booleanos).

---

## 7.3 Métodos de transformação e limpeza

- `s.lower()` e `s.upper()`: Converte para minúsculas ou maiúsculas.
- `s.strip()`: Remove espaços em branco (ou caracteres especificados) do início e do fim.
- `s.replace(antigo, novo)`: Substitui todas as ocorrências de `antigo` por `novo`.
- `s.split(separador)`: Divide a string em uma lista de strings.
- `separador.join(lista)`: Une elementos de uma lista em uma única string.

---

## 7.4 Formatação avançada

```python
# Alinhamento e preenchimento
print(f"{'centro':^20}")  # Centralizado em 20 caracteres
print(f"{'esquerda':<20}") # Alinhado à esquerda
print(f"{'direita':>20}")  # Alinhado à direita
```

---

## 7.5 Projeto Prático: Jogo da Forca

O capítulo consolida a manipulação de strings e coleções implementando o clássico jogo da forca com gráficos ASCII e controle de tentativas.
