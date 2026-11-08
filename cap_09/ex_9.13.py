"""
Exercício 9.13 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que imprima as linhas de um arquivo-texto que contenham
uma determinada palavra informada na linha de comando (semelhante ao grep).
"""

import sys
import os


def buscar_palavra_no_arquivo(nome_arquivo, termo_busca, case_sensitive=False):
    if not os.path.exists(nome_arquivo):
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return

    termo = termo_busca if case_sensitive else termo_busca.lower()
    encontrou = False

    with open(nome_arquivo, "r", encoding="utf-8") as f:
        for num_linha, linha in enumerate(f, start=1):
            linha_comparacao = linha if case_sensitive else linha.lower()
            if termo in linha_comparacao:
                print(f"Linha {num_linha:03d}: {linha.rstrip()}")
                encontrou = True

    if not encontrou:
        print(f"O termo '{termo_busca}' não foi encontrado no arquivo.")


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        arquivo = sys.argv[1]
        termo = sys.argv[2]
        buscar_palavra_no_arquivo(arquivo, termo)
    else:
        # Demonstração autônoma
        f_temp = "temp_grep.txt"
        with open(f_temp, "w", encoding="utf-8") as f:
            f.write("Primeira linha sem o termo chave.\n")
            f.write("Segunda linha contendo Python como linguagem.\n")
            f.write("Terceira linha comum.\n")
            f.write("Quarta linha com outro Python de exemplo.\n")

        print("--- Buscando 'Python' no arquivo de teste ---")
        buscar_palavra_no_arquivo(f_temp, "Python")

        if os.path.exists(f_temp):
            os.remove(f_temp)
