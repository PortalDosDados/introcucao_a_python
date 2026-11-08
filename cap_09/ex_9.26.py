"""
Exercício 9.26 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que leia um arquivo-texto e o divida em múltiplos arquivos
menores, contendo no máximo n linhas cada um (estilo utilitário split).
"""

import os
import sys


def dividir_arquivo(arquivo_origem, linhas_por_parte=5, prefixo="parte"):
    if not os.path.exists(arquivo_origem):
        print(f"Erro: Arquivo '{arquivo_origem}' não encontrado.")
        return []

    arquivos_gerados = []
    num_parte = 1
    linhas_gravadas = 0
    saida_atual = None

    with open(arquivo_origem, "r", encoding="utf-8") as entrada:
        for linha in entrada:
            if linhas_gravadas == 0:
                nome_parte = f"{prefixo}_{num_parte:03d}.txt"
                saida_atual = open(nome_parte, "w", encoding="utf-8")
                arquivos_gerados.append(nome_parte)

            saida_atual.write(linha)
            linhas_gravadas += 1

            if linhas_gravadas >= linhas_por_parte:
                saida_atual.close()
                linhas_gravadas = 0
                num_parte += 1

    if saida_atual and not saida_atual.closed:
        saida_atual.close()

    print(f"Arquivo dividido em {len(arquivos_gerados)} parte(s).")
    return arquivos_gerados


if __name__ == "__main__":
    origem = "temp_origem_split.txt"
    with open(origem, "w", encoding="utf-8") as f:
        for i in range(1, 14):
            f.write(f"Linha de teste número {i}\n")

    gerados = dividir_arquivo(origem, linhas_por_parte=5, prefixo="temp_split")

    for arq in gerados:
        print(f"\n--- {arq} ---")
        with open(arq, "r", encoding="utf-8") as f:
            print(f.read(), end="")

    for arq in [origem] + gerados:
        if os.path.exists(arq):
            os.remove(arq)
