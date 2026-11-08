"""
Exercício 9.31 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que receba um caminho do sistema pela linha de comando
e informe se ele existe, e caso exista, se trata-se de um arquivo ou de um diretório.
"""

import os
import sys


def inspecionar_caminho(caminho):
    if not os.path.exists(caminho):
        print(f"O caminho '{caminho}' NÃO existe no sistema.")
        return "inexistente"

    if os.path.isdir(caminho):
        print(f"O caminho '{caminho}' é um DIRETÓRIO existente.")
        return "diretorio"
    elif os.path.isfile(caminho):
        tamanho = os.path.getsize(caminho)
        print(f"O caminho '{caminho}' é um ARQUIVO existente ({tamanho} bytes).")
        return "arquivo"
    else:
        print(f"O caminho '{caminho}' é um tipo especial do sistema.")
        return "outro"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        inspecionar_caminho(sys.argv[1])
    else:
        # Demonstração autônoma
        print("--- Testando com pasta atual '.' ---")
        inspecionar_caminho(".")

        print("\n--- Testando com arquivo existente ---")
        inspecionar_caminho("README.md")

        print("\n--- Testando com caminho inexistente ---")
        inspecionar_caminho("caminho_inexistente_123.xyz")
