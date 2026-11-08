"""
Exercício 9.14 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que leia um arquivo-texto e elimine os espaços em branco
repetidos entre palavras, gerando um novo arquivo de saída limpo.
"""

import sys
import os


def eliminar_espacos_repetidos(arquivo_entrada, arquivo_saida):
    if not os.path.exists(arquivo_entrada):
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")
        return

    with (
        open(arquivo_entrada, "r", encoding="utf-8") as entrada,
        open(arquivo_saida, "w", encoding="utf-8") as saida,
    ):
        for linha in entrada:
            palavras = linha.split()
            linha_formatada = " ".join(palavras) + "\n"
            saida.write(linha_formatada)


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        eliminar_espacos_repetidos(sys.argv[1], sys.argv[2])
    else:
        # Demonstração autônoma
        f_in, f_out = "temp_espacoso.txt", "temp_limpo.txt"
        with open(f_in, "w", encoding="utf-8") as f:
            f.write("Este    texto    tem      muitos   espacos.\n")
            f.write("Outra     linha    com   espacamento   excessivo.\n")

        eliminar_espacos_repetidos(f_in, f_out)

        print(f"--- Texto limpo em '{f_out}' ---")
        with open(f_out, "r", encoding="utf-8") as res:
            print(res.read(), end="")

        for f in [f_in, f_out]:
            if os.path.exists(f):
                os.remove(f)
