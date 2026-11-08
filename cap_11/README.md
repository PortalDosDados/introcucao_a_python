# Capítulo 11 ■ Banco de Dados (SQLite)

O Python inclui nativamente na sua biblioteca padrão o módulo `sqlite3`, que permite interagir com o SQLite — um sistema de gerenciamento de banco de dados relacional (SGBD) embutido, transacional (ACID), leve e que armazena os dados em um único arquivo de disco (ou na memória RAM).

---

## 11.1 Conexão e Criação de Tabelas

Para trabalhar com o SQLite, primeiro conectamos ao arquivo de banco de dados e obtemos um cursor para executar comandos SQL:

```python
import sqlite3

conexao = sqlite3.connect("mercado.db")
cursor = conexao.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS precos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    )
"""
)

conexao.commit()
cursor.close()
conexao.close()
```

---

## 11.2 Inserção de Registros (`INSERT`)

Para evitar vulnerabilidades de **Injeção de SQL (SQL Injection)**, nunca utilize concatenação de strings para montar comandos SQL. Sempre utilize **placeholders** (`?` ou `:nome`):

```python
# Modo Seguro com tupla de parâmetros
cursor.execute("INSERT INTO precos (nome, preco) VALUES (?, ?)", ("Tomate", 8.50))
conexao.commit()
```

---

## 11.3 Consultando Dados (`SELECT`)

- `cursor.fetchall()`: Retorna todas as linhas da consulta como uma lista de tuplas.
- `cursor.fetchone()`: Retorna a próxima linha individual ou `None` se a consulta não tiver mais resultados.

```python
cursor.execute("SELECT nome, preco FROM precos ORDER BY preco ASC")
for linha in cursor.fetchall():
    print(f"Produto: {linha[0]} | Preço: R$ {linha[1]:.2f}")
```

---

## 11.4 Atualização e Remoção (`UPDATE` e `DELETE`)

Modificações nos dados exigem o método `conexao.commit()` para serem gravadas permanentemente no disco:

```python
# Atualizar preço de um produto específico
cursor.execute("UPDATE precos SET preco = ? WHERE nome = ?", (9.20, "Tomate"))
conexao.commit()
print(f"Linhas alteradas: {cursor.rowcount}")

# Excluir registros
cursor.execute("DELETE FROM precos WHERE preco > ?", (100.00,))
conexao.commit()
```

---

## 11.5 Bancos de Dados em Memória (`:memory:`)

Para testes rápidos, prototipagem ou ambientes de desenvolvimento sem necessidade de persistência em arquivo físico, podemos abrir um banco temporário na memória RAM usando `sqlite3.connect(":memory:")`.
