"""
Exercício 9.1 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Escreva um programa que receba o nome de um arquivo pela linha de comando
e que imprima todas as suas linhas na tela.
"""

import sys
import os


def imprimir_arquivo(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return

    with open(nome_arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            print(linha, end="")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        imprimir_arquivo(sys.argv[1])
    else:
        # Demonstração autônoma caso executado sem argumentos
        arquivo_temp = "temp_ex9_1.txt"
        with open(arquivo_temp, "w", encoding="utf-8") as temp:
            temp.write("Linha 1: Introdução a Python\n")
            temp.write("Linha 2: Manipulação de Arquivos\n")
            temp.write("Linha 3: Concluído com sucesso\n")

        print(f"--- Conteúdo de '{arquivo_temp}' ---")
        imprimir_arquivo(arquivo_temp)

        if os.path.exists(arquivo_temp):
            os.remove(arquivo_temp)
