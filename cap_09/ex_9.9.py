"""
Exercício 9.9 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que receba uma lista de nomes de arquivos pela linha de
comando e imprima o conteúdo de cada um deles paginado na tela.
"""

import sys
import os


def imprimir_paginado(lista_arquivos, linhas_por_pagina=60):
    for nome_arquivo in lista_arquivos:
        if not os.path.exists(nome_arquivo):
            print(f"\nAviso: Arquivo '{nome_arquivo}' não encontrado.\n")
            continue

        num_pagina = 1
        linhas_na_pagina = 0

        print(f"\n{'=' * 50}")
        print(f"Arquivo: {nome_arquivo} | Página {num_pagina}")
        print(f"{'=' * 50}")

        with open(nome_arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                if linhas_na_pagina >= linhas_por_pagina:
                    num_pagina += 1
                    print(f"\n{'=' * 50}")
                    print(f"Arquivo: {nome_arquivo} | Página {num_pagina}")
                    print(f"{'=' * 50}")
                    linhas_na_pagina = 0

                print(linha, end="")
                linhas_na_pagina += 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        imprimir_paginado(sys.argv[1:])
    else:
        # Demonstração autônoma
        f1, f2 = "temp_relat1.txt", "temp_relat2.txt"
        with open(f1, "w", encoding="utf-8") as a:
            for i in range(1, 5):
                a.write(f"Relatório A - Item {i}\n")
        with open(f2, "w", encoding="utf-8") as b:
            for i in range(1, 5):
                b.write(f"Relatório B - Item {i}\n")

        imprimir_paginado([f1, f2], linhas_por_pagina=2)

        for f in [f1, f2]:
            if os.path.exists(f):
                os.remove(f)
