"""
Exercício 9.5 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que inverta a ordem das linhas de um arquivo de entrada
(a primeira linha se torna a última, a segunda a penúltima, etc.),
gravando o resultado em um arquivo de saída ou imprimindo na tela.
"""

import sys
import os


def inverter_arquivo(arquivo_entrada, arquivo_saida=None):
    if not os.path.exists(arquivo_entrada):
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")
        return

    with open(arquivo_entrada, "r", encoding="utf-8") as entrada:
        linhas = entrada.readlines()

    linhas_invertidas = linhas[::-1]

    if arquivo_saida:
        with open(arquivo_saida, "w", encoding="utf-8") as saida:
            saida.writelines(linhas_invertidas)
    else:
        for linha in linhas_invertidas:
            print(linha, end="")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        saida = sys.argv[2] if len(sys.argv) >= 3 else None
        inverter_arquivo(sys.argv[1], saida)
    else:
        # Demonstração autônoma
        f_in, f_out = "temp_orig.txt", "temp_inv.txt"
        with open(f_in, "w", encoding="utf-8") as f:
            f.write("Linha 1\nLinha 2\nLinha 3\nLinha 4\n")

        inverter_arquivo(f_in, f_out)

        print(f"--- Linhas invertidas em '{f_out}' ---")
        with open(f_out, "r", encoding="utf-8") as res:
            print(res.read(), end="")

        for f in [f_in, f_out]:
            if os.path.exists(f):
                os.remove(f)
