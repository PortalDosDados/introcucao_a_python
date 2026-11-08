"""
Exercício 11.2 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Faça um programa para listar todos os registros da tabela precos criada no
exercício anterior, formatando o preço com duas casas decimais e alinhando
as colunas com cabeçalho.
"""

import sqlite3
import os


def listar_tabela_precos(banco="precos.db"):
    if not os.path.exists(banco):
        print(f"Erro: Banco de dados '{banco}' não encontrado.")
        return

    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, preco FROM precos ORDER BY id")
    registros = cursor.fetchall()

    print(f"\n{'ID':<5} {'PRODUTO':<25} {'PREÇO (R$)':>10}")
    print("-" * 42)

    for id_prod, nome, preco in registros:
        print(f"{id_prod:<5} {nome:<25} {preco:>10.2f}")

    print("-" * 42)
    print(f"Total de registros: {len(registros)}\n")

    cursor.close()
    conexao.close()


if __name__ == "__main__":
    banco_demo = "temp_precos_ex11_2.db"
    conexao = sqlite3.connect(banco_demo)
    cursor = conexao.cursor()
    cursor.execute(
        "CREATE TABLE precos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco REAL)"
    )
    cursor.executemany(
        "INSERT INTO precos (nome, preco) VALUES (?, ?)",
        [("Maçã", 6.30), ("Banana Prata", 4.90), ("Laranja Lima", 5.50)],
    )
    conexao.commit()
    cursor.close()
    conexao.close()

    listar_tabela_precos(banco_demo)

    if os.path.exists(banco_demo):
        os.remove(banco_demo)
