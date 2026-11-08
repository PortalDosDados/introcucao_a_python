"""
Exercício 11.1 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um banco de dados para armazenar os dados de preços de produtos de um mercado.
A tabela precos deve ter as seguintes colunas:
- nome (texto)
- preco (real)
Insira pelo menos 3 registros e consulte-os exibindo o resultado formatado.
"""

import sqlite3
import os

BANCO_DADOS = "precos.db"


def inicializar_banco(banco=BANCO_DADOS):
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS precos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            preco REAL NOT NULL
        )
    """)
    conexao.commit()
    cursor.close()
    conexao.close()


def inserir_produtos(produtos, banco=BANCO_DADOS):
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()
    for nome, preco in produtos:
        cursor.execute(
            """
            INSERT OR REPLACE INTO precos (nome, preco)
            VALUES (?, ?)
        """,
            (nome, preco),
        )
    conexao.commit()
    cursor.close()
    conexao.close()


def consultar_produtos(banco=BANCO_DADOS):
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, preco FROM precos ORDER BY nome")
    registros = cursor.fetchall()
    cursor.close()
    conexao.close()
    return registros


if __name__ == "__main__":
    banco_demo = "temp_precos_ex11_1.db"
    inicializar_banco(banco_demo)

    produtos_iniciais = [
        ("Batata", 4.50),
        ("Tomate", 7.80),
        ("Cebola", 5.20),
        ("Arroz 5kg", 26.90),
    ]

    inserir_produtos(produtos_iniciais, banco_demo)
    resultados = consultar_produtos(banco_demo)

    print("--- Produtos Cadastrados no Banco ---")
    for nome, preco in resultados:
        print(f"Produto: {nome:15s} | Preço: R$ {preco:6.2f}")

    if os.path.exists(banco_demo):
        os.remove(banco_demo)
