"""
Exercício 9.11 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que leia um arquivo texto e conte a ocorrência de cada palavra
no texto, exibindo um relatório com as palavras e suas respectivas frequências.
"""

import sys
import os
import string


def contar_palavras(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return {}

    contagem = {}
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            # Remove pontuações e converte para minúsculas
            linha_limpa = linha.lower()
            for pontuacao in string.punctuation:
                linha_limpa = linha_limpa.replace(pontuacao, " ")

            palavras = linha_limpa.split()
            for p in palavras:
                contagem[p] = contagem.get(p, 0) + 1

    return contagem


if __name__ == "__main__":
    if len(sys.argv) > 1:
        resultado = contar_palavras(sys.argv[1])
        for palavra, freq in sorted(resultado.items()):
            print(f"{palavra}: {freq}")
    else:
        # Demonstração autônoma
        f_temp = "temp_texto_contagem.txt"
        with open(f_temp, "w", encoding="utf-8") as f:
            f.write(
                "Python e simples. Python e poderoso. Aprender Python e divertido!\n"
            )

        resultado = contar_palavras(f_temp)
        print("--- Frequência de Palavras ---")
        for palavra, freq in sorted(
            resultado.items(), key=lambda item: item[1], reverse=True
        ):
            print(f"'{palavra}': {freq} ocorrência(s)")

        if os.path.exists(f_temp):
            os.remove(f_temp)
