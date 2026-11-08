"""
Exercício 11.3 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Escreva um programa que realize uma consulta na tabela precos baseando-se no
nome do produto informado pelo usuário. Se o produto for encontrado, mostre
seu preço; caso contrário, exiba uma mensagem informativa (utilizando placeholders
? para prevenir SQL Injection).
"""

import sqlite3
import os
import sys


def buscar_preco_produto(nome_produto, banco="precos.db"):
    conexao = sqlite3.connect(banco)
    cursor = conexao.cursor()

    # Consulta parametrizada segura
    cursor.execute(
        "SELECT preco FROM precos WHERE lower(nome) = lower(?)", (nome_produto.strip(),)
    )
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado is not None:
        print(f"Produto: {nome_produto} | Preço: R$ {resultado[0]:.2f}")
        return resultado[0]
    else:
        print(f"Aviso: Produto '{nome_produto}' não encontrado no banco de dados.")
        return None


if __name__ == "__main__":
    banco_demo = "temp_precos_ex11_3.db"
    conexao = sqlite3.connect(banco_demo)
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE precos (nome TEXT, preco REAL)")
    cursor.executemany(
        "INSERT INTO precos VALUES (?, ?)",
        [("Feijão Carioca", 8.90), ("Azeite de Oliva", 34.50)],
    )
    conexao.commit()
    cursor.close()
    conexao.close()

    print("--- Teste de busca com produto existente ---")
    buscar_preco_produto("Feijão Carioca", banco_demo)

    print("\n--- Teste de busca com produto inexistente ---")
    buscar_preco_produto("Chocolate", banco_demo)

    if os.path.exists(banco_demo):
        os.remove(banco_demo)
