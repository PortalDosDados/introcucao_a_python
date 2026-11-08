"""
Exercício 9.27 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que faça o processo inverso do exercício anterior: receba uma
lista de arquivos parciais e reúna seu conteúdo em um único arquivo de saída.
"""

import os
import sys


def unir_partes_arquivo(lista_partes, arquivo_destino):
    partes_ordenadas = sorted(lista_partes)
    total_linhas = 0

    with open(arquivo_destino, "w", encoding="utf-8") as saida:
        for parte in partes_ordenadas:
            if not os.path.exists(parte):
                print(f"Aviso: Parte '{parte}' não encontrada.")
                continue

            with open(parte, "r", encoding="utf-8") as entrada:
                for linha in entrada:
                    saida.write(linha)
                    total_linhas += 1

    print(f"Arquivo reunido em '{arquivo_destino}' ({total_linhas} linhas).")
    return total_linhas


if __name__ == "__main__":
    partes = ["temp_p1.txt", "temp_p2.txt"]
    with open(partes[0], "w", encoding="utf-8") as f1:
        f1.write("Linha 1 da parte 1\nLinha 2 da parte 1\n")
    with open(partes[1], "w", encoding="utf-8") as f2:
        f2.write("Linha 3 da parte 2\nLinha 4 da parte 2\n")

    destino = "temp_unido_completo.txt"
    unir_partes_arquivo(partes, destino)

    print(f"\n--- Conteúdo Reunido ({destino}) ---")
    with open(destino, "r", encoding="utf-8") as f:
        print(f.read(), end="")

    for f in partes + [destino]:
        if os.path.exists(f):
            os.remove(f)
