"""
Exercício 11.4 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Modifique o programa de consulta para permitir a busca de produtos por faixa
de valores (preço mínimo e preço máximo informados pelo usuário), exibindo todos
os produtos encontrados dentro do intervalo especificado, ordenados pelo valor.
"""

import sqlite3
import os


def buscar_produtos_por_faixa_preco(preco_min, preco_max, banco="precos.db"):
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT nome, preco
        FROM precos
        WHERE preco >= ? AND preco <= ?
        ORDER BY preco ASC
    """,
        (preco_min, preco_max),
    )

    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()

    print(f"\nProdutos com preço entre R$ {preco_min:.2f} e R$ {preco_max:.2f}:")
    print("-" * 40)
    if not resultados:
        print("Nenhum produto encontrado nessa faixa de preço.")
    else:
        for nome, preco in resultados:
            print(f"- {nome:<25} R$ {preco:>6.2f}")
    print("-" * 40)
    return resultados


if __name__ == "__main__":
    banco_demo = "temp_precos_ex11_4.db"
    conexao = sqlite3.connect(banco_demo)
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE precos (nome TEXT, preco REAL)")
    cursor.executemany(
        "INSERT INTO precos VALUES (?, ?)",
        [
            ("Pão Francês (kg)", 14.00),
            ("Leite Integral", 4.90),
            ("Queijo Mussarela", 42.00),
            ("Manteiga 200g", 12.50),
            ("Café Torrado 500g", 18.90),
        ],
    )
    conexao.commit()
    cursor.close()
    conexao.close()

    buscar_produtos_por_faixa_preco(10.00, 20.00, banco_demo)

    if os.path.exists(banco_demo):
        os.remove(banco_demo)
