# Capítulo 6 ■ Listas, Dicionários, Tuplas e Conjuntos

Coleções de dados permitem armazenar e manipular múltiplos valores sob um único identificador.

---

## 6.1 Listas

Uma lista em Python é uma sequência mutável de elementos, definida por colchetes `[]`.

```python
notas = [6, 7, 5, 8, 9]
print(notas[0])  # Primeiro elemento: 6
print(len(notas))  # Tamanho da lista: 5
```

- **Fatiamento (*slicing*)**: `lista[inicio:fim]` copia do índice `inicio` até `fim - 1`.
- **Adição**: `lista.append(elemento)` adiciona ao fim; `lista.extend(outra)` ou `+` concatena.
- **Remoção**: `del lista[indice]` remove por posição; `lista.pop(indice)` remove e retorna.

---

## 6.2 Filas (FIFO) e Pilhas (LIFO)

- **Fila (First In, First Out)**: Novos elementos entram no fim (`append`) e são atendidos pelo início (`pop(0)`).
- **Pilha (Last In, First Out)**: Novos elementos entram no topo (`append`) e são retirados do topo (`pop()`).

---

## 6.3 O Laço `for`

O laço `for` itera diretamente sobre os elementos de uma sequência sem a necessidade de controle manual de índices:

```python
for item in lista:
    print(item)
```

Com `range(inicio, fim, passo)`:

```python
for i in range(1, 11):
    print(i)
```

---

## 6.4 Dicionários

Dicionários associam **chaves únicas** a **valores**, delimitados por chaves `{}`.

```python
tabela = {"Alface": 0.45, "Batata": 1.20, "Tomate": 2.30}
print(tabela["Batata"])  # 1.20
```

---

## 6.5 Tuplas e Conjuntos

- **Tuplas**: Sequências imutáveis definidas por parênteses `()`.
- **Conjuntos (`set`)**: Coleções não ordenadas de elementos únicos, com suporte a operações matemáticas de união (`|`), interseção (`&`) e diferença (`-`).
