"""
Exercício 11.5 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Escreva um programa que aplique um reajuste percentual em todos os produtos da
tabela precos (por exemplo, um aumento de 10% informado pelo usuário),
utilizando o comando SQL UPDATE e confirmando a operação com commit.
"""

import sqlite3
import os


def reajustar_precos_percentual(percentual_aumento, banco="precos.db"):
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()

    # Fator de multiplicação: ex.: 10% de aumento -> fator = 1 + (10 / 100) = 1.10
    fator = 1.0 + (percentual_aumento / 100.0)

    cursor.execute(
        """
        UPDATE precos
        SET preco = round(preco * ?, 2)
    """,
        (fator,),
    )

    linhas_afetadas = cursor.rowcount
    conexao.commit()
    cursor.close()
    conexao.close()

    print(
        f"Reajuste de {percentual_aumento:+.1f}% aplicado em {linhas_afetadas} produto(s)."
    )
    return linhas_afetadas


if __name__ == "__main__":
    banco_demo = "temp_precos_ex11_5.db"
    conexao = sqlite3.connect(banco_demo)
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE precos (nome TEXT, preco REAL)")
    cursor.executemany(
        "INSERT INTO precos VALUES (?, ?)",
        [("Arroz", 20.00), ("Feijão", 10.00), ("Macarrão", 5.00)],
    )
    conexao.commit()
    cursor.close()
    conexao.close()

    print("Preços antes do reajuste:")
    conexao = sqlite3.connect(banco_demo)
    for row in conexao.execute("SELECT nome, preco FROM precos"):
        print(f"  {row[0]}: R$ {row[1]:.2f}")
    conexao.close()

    reajustar_precos_percentual(10.0, banco_demo)

    print("\nPreços após reajuste de +10%:")
    conexao = sqlite3.connect(banco_demo)
    for row in conexao.execute("SELECT nome, preco FROM precos"):
        print(f"  {row[0]}: R$ {row[1]:.2f}")
    conexao.close()

    if os.path.exists(banco_demo):
        os.remove(banco_demo)
