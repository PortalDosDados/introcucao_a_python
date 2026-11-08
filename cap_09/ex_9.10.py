"""
Exercício 9.10 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que receba uma lista de nomes de arquivos pela linha de
comando e que gere um único arquivo de saída contendo o conteúdo de todos eles
combinados em sequência.
"""

import sys
import os


def concatenar_multiplos_arquivos(lista_arquivos_entrada, arquivo_saida):
    with open(arquivo_saida, "w", encoding="utf-8") as saida:
        for nome_arquivo in lista_arquivos_entrada:
            if not os.path.exists(nome_arquivo):
                print(f"Aviso: Arquivo '{nome_arquivo}' ignorado (não encontrado).")
                continue

            with open(nome_arquivo, "r", encoding="utf-8") as entrada:
                for linha in entrada:
                    saida.write(linha)


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        # Último argumento é a saída, os anteriores são as entradas
        saida_destino = sys.argv[-1]
        entradas = sys.argv[1:-1]
        concatenar_multiplos_arquivos(entradas, saida_destino)
    else:
        # Demonstração autônoma
        arquivos = ["temp_c1.txt", "temp_c2.txt", "temp_c3.txt"]
        for idx, arq in enumerate(arquivos, start=1):
            with open(arq, "w", encoding="utf-8") as f:
                f.write(f"Conteúdo do Bloco {idx}\n")

        f_saida = "temp_todos_unidos.txt"
        concatenar_multiplos_arquivos(arquivos, f_saida)

        print(f"--- Conteúdo unificado em '{f_saida}' ---")
        with open(f_saida, "r", encoding="utf-8") as res:
            print(res.read(), end="")

        for f in arquivos + [f_saida]:
            if os.path.exists(f):
                os.remove(f)
