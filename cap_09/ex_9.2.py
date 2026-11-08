"""
Exercício 9.2 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Modifique o programa anterior para também receber o número da linha de início
e da linha de fim a imprimir.
"""

import sys
import os


def imprimir_linhas(nome_arquivo, linha_inicio, linha_fim):
    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return

    with open(nome_arquivo, "r", encoding="utf-8") as f:
        for num_linha, linha in enumerate(f, start=1):
            if linha_inicio <= num_linha <= linha_fim:
                print(f"[{num_linha:02d}] {linha}", end="")


if __name__ == "__main__":
    if len(sys.argv) >= 4:
        arquivo = sys.argv[1]
        inicio = int(sys.argv[2])
        fim = int(sys.argv[3])
        imprimir_linhas(arquivo, inicio, fim)
    else:
        # Demonstração autônoma
        arquivo_temp = "temp_ex9_2.txt"
        with open(arquivo_temp, "w", encoding="utf-8") as temp:
            for i in range(1, 11):
                temp.write(f"Registro número {i}\n")

        print("--- Imprimindo da linha 3 até a linha 7 ---")
        imprimir_linhas(arquivo_temp, 3, 7)

        if os.path.exists(arquivo_temp):
            os.remove(arquivo_temp)
