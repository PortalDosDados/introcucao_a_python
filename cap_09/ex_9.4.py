"""
Exercício 9.4 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que receba o nome de dois arquivos como parâmetros da linha
de comando e que gere um arquivo de saída com as linhas do primeiro e do segundo
arquivo intercaladas.
"""

import sys
import os


def intercalar_arquivos(arquivo1, arquivo2, arquivo_saida):
    with (
        open(arquivo1, "r", encoding="utf-8") as a1,
        open(arquivo2, "r", encoding="utf-8") as a2,
        open(arquivo_saida, "w", encoding="utf-8") as saida,
    ):
        while True:
            l1 = a1.readline()
            l2 = a2.readline()

            if not l1 and not l2:
                break

            if l1:
                saida.write(l1 if l1.endswith("\n") else l1 + "\n")
            if l2:
                saida.write(l2 if l2.endswith("\n") else l2 + "\n")


if __name__ == "__main__":
    if len(sys.argv) >= 4:
        intercalar_arquivos(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        # Demonstração autônoma
        f1, f2, fout = "temp_par.txt", "temp_impar.txt", "temp_intercalado.txt"
        with open(f1, "w", encoding="utf-8") as a:
            a.write("A1\nA2\nA3\n")
        with open(f2, "w", encoding="utf-8") as b:
            b.write("B1\nB2\nB3\n")

        intercalar_arquivos(f1, f2, fout)

        print(f"--- Linhas intercaladas em '{fout}' ---")
        with open(fout, "r", encoding="utf-8") as res:
            print(res.read(), end="")

        for f in [f1, f2, fout]:
            if os.path.exists(f):
                os.remove(f)
