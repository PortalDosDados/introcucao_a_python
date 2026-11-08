"""
Exercício 9.34 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que meça o tempo de processamento/leitura de um arquivo grande,
calculando e exibindo o tempo decorrido em segundos e o tamanho processado.
"""

import os
import sys
import time


def medir_tempo_leitura(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return

    inicio = time.time()
    tamanho_total = 0
    total_linhas = 0

    with open(nome_arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            tamanho_total += len(linha)
            total_linhas += 1

    fim = time.time()
    duracao = fim - inicio

    print(f"\n--- Estatísticas de Leitura ---")
    print(f"Arquivo: {nome_arquivo}")
    print(f"Total de linhas: {total_linhas}")
    print(
        f"Tamanho processado: {tamanho_total} caracteres ({os.path.getsize(nome_arquivo)} bytes)"
    )
    print(f"Tempo total gasto: {duracao:.6f} segundos")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        medir_tempo_leitura(sys.argv[1])
    else:
        # Demonstração autônoma
        f_temp = "temp_benchmark.txt"
        with open(f_temp, "w", encoding="utf-8") as f:
            for i in range(10000):
                f.write(
                    f"Linha de benchmark com número {i} para teste de velocidade.\n"
                )

        medir_tempo_leitura(f_temp)

        if os.path.exists(f_temp):
            os.remove(f_temp)
