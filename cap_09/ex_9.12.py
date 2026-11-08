"""
Exercício 9.12 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Modifique o programa anterior para também registrar a linha e a coluna
(ou posições) onde cada palavra aparece no arquivo.
"""

import sys
import os
import string


def mapear_posicoes_palavras(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return {}

    mapa = {}  # {palavra: [(linha, coluna), ...]}

    with open(nome_arquivo, "r", encoding="utf-8") as f:
        for num_linha, linha in enumerate(f, start=1):
            coluna = 0
            palavra_atual = ""
            coluna_inicio = 0

            for col_idx, caractere in enumerate(linha):
                if caractere.isalnum():
                    if not palavra_atual:
                        coluna_inicio = col_idx + 1
                    palavra_atual += caractere.lower()
                else:
                    if palavra_atual:
                        if palavra_atual not in mapa:
                            mapa[palavra_atual] = []
                        mapa[palavra_atual].append((num_linha, coluna_inicio))
                        palavra_atual = ""

            if palavra_atual:
                if palavra_atual not in mapa:
                    mapa[palavra_atual] = []
                mapa[palavra_atual].append((num_linha, coluna_inicio))

    return mapa


if __name__ == "__main__":
    if len(sys.argv) > 1:
        mapa = mapear_posicoes_palavras(sys.argv[1])
        for p, posicoes in sorted(mapa.items()):
            print(f"{p}: {posicoes}")
    else:
        # Demonstração autônoma
        f_temp = "temp_posicoes.txt"
        with open(f_temp, "w", encoding="utf-8") as f:
            f.write("ola mundo\nola python mundo\n")

        mapa = mapear_posicoes_palavras(f_temp)
        print("--- Posições das Palavras (Linha, Coluna) ---")
        for p, posicoes in sorted(mapa.items()):
            pos_str = ", ".join([f"(L:{l}, C:{c})" for l, c in posicoes])
            print(f"'{p}': {pos_str}")

        if os.path.exists(f_temp):
            os.remove(f_temp)
