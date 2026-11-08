"""
Exercício 9.28 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que compare dois arquivos texto e exiba as diferenças entre
eles, indicando as linhas divergentes em cada arquivo (semelhante ao comando diff).
"""

import os
import sys


def comparar_arquivos(arquivo1, arquivo2):
    if not os.path.exists(arquivo1) or not os.path.exists(arquivo2):
        print("Erro: Um ou ambos os arquivos não foram encontrados.")
        return

    with (
        open(arquivo1, "r", encoding="utf-8") as f1,
        open(arquivo2, "r", encoding="utf-8") as f2,
    ):
        linhas1 = f1.readlines()
        linhas2 = f2.readlines()

    max_linhas = max(len(linhas1), len(linhas2))
    diferencas = 0

    print(f"Comparando '{arquivo1}' com '{arquivo2}':\n")
    for i in range(max_linhas):
        l1 = linhas1[i].rstrip("\r\n") if i < len(linhas1) else "<fim do arquivo>"
        l2 = linhas2[i].rstrip("\r\n") if i < len(linhas2) else "<fim do arquivo>"

        if l1 != l2:
            diferencas += 1
            print(f"Linha {i + 1:03d} difere:")
            print(f"  < {l1}")
            print(f"  > {l2}")

    if diferencas == 0:
        print("Os arquivos são idênticos.")
    else:
        print(f"\nTotal de linhas divergentes: {diferencas}")


if __name__ == "__main__":
    a1, a2 = "temp_diff1.txt", "temp_diff2.txt"
    with open(a1, "w", encoding="utf-8") as f:
        f.write("Primeira linha\nSegunda linha original\nTerceira linha\n")
    with open(a2, "w", encoding="utf-8") as f:
        f.write(
            "Primeira linha\nSegunda linha modificada\nTerceira linha\nQuarta nova linha\n"
        )

    comparar_arquivos(a1, a2)

    for f in [a1, a2]:
        if os.path.exists(f):
            os.remove(f)
