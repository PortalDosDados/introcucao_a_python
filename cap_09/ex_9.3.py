"""
Exercício 9.3 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que leia dois arquivos e gere um terceiro com o conteúdo
dos dois primeiros, na ordem em que foram passados na linha de comando.
"""

import sys
import os


def concatenar_arquivos(arquivo1, arquivo2, arquivo_saida):
    with open(arquivo_saida, "w", encoding="utf-8") as saida:
        for arq in [arquivo1, arquivo2]:
            if os.path.exists(arq):
                with open(arq, "r", encoding="utf-8") as entrada:
                    for linha in entrada:
                        saida.write(linha)
            else:
                print(f"Aviso: Arquivo '{arq}' não encontrado.")


if __name__ == "__main__":
    if len(sys.argv) >= 4:
        concatenar_arquivos(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        # Demonstração autônoma
        f1, f2, fout = "temp_p1.txt", "temp_p2.txt", "temp_concatenado.txt"
        with open(f1, "w", encoding="utf-8") as a:
            a.write("Parte 1 - Linha A\nParte 1 - Linha B\n")
        with open(f2, "w", encoding="utf-8") as b:
            b.write("Parte 2 - Linha C\nParte 2 - Linha D\n")

        concatenar_arquivos(f1, f2, fout)

        print(f"--- Conteúdo gerado em '{fout}' ---")
        with open(fout, "r", encoding="utf-8") as res:
            print(res.read(), end="")

        for f in [f1, f2, fout]:
            if os.path.exists(f):
                os.remove(f)
