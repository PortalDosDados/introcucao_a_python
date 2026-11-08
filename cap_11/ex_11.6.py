"""
Exercício 11.6 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Escreva um programa que solicite o nome de um produto e um novo preço para
atualização na tabela precos. Verifique se o registro foi efetivamente alterado
utilizando cursor.rowcount. Caso nenhuma linha tenha sido afetada (rowcount == 0),
exiba uma mensagem informando que o produto não foi encontrado.
"""

import sqlite3
import os


def alterar_preco_produto(nome_produto, novo_preco, banco="precos.db"):
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()

    cursor.execute(
        """
        UPDATE precos
        SET preco = ?
        WHERE lower(nome) = lower(?)
    """,
        (novo_preco, nome_produto.strip()),
    )

    linhas_alteradas = cursor.rowcount
    conexao.commit()
    cursor.close()
    conexao.close()

    if linhas_alteradas > 0:
        print(
            f"Sucesso: O preço de '{nome_produto}' foi atualizado para R$ {novo_preco:.2f}."
        )
        return True
    else:
        print(f"Erro: O produto '{nome_produto}' não foi encontrado para atualização.")
        return False


if __name__ == "__main__":
    banco_demo = "temp_precos_ex11_6.db"
    conexao = sqlite3.connect(banco_demo)
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE precos (nome TEXT, preco REAL)")
    cursor.execute("INSERT INTO precos VALUES (?, ?)", ("Sabonete", 2.50))
    conexao.commit()
    cursor.close()
    conexao.close()

    print("--- Tentativa 1: Atualização de produto existente ('Sabonete') ---")
    alterar_preco_produto("Sabonete", 3.10, banco_demo)

    print("\n--- Tentativa 2: Atualização de produto inexistente ('Detergente') ---")
    alterar_preco_produto("Detergente", 4.00, banco_demo)

    if os.path.exists(banco_demo):
        os.remove(banco_demo)
