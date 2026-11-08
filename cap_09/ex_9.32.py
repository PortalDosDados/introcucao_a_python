"""
Exercício 9.32 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que receba o nome de um diretório pela linha de comando
e liste todos os seus arquivos e subdiretórios, diferenciando-os.
"""

import os
import sys


def listar_diretorio(caminho="."):
    if not os.path.exists(caminho):
        print(f"Erro: O caminho '{caminho}' não existe.")
        return

    if not os.path.isdir(caminho):
        print(f"Erro: '{caminho}' não é um diretório.")
        return

    print(f"\nConteúdo do diretório: {os.path.abspath(caminho)}")
    print("-" * 50)

    itens = os.listdir(caminho)
    pastas = []
    arquivos = []

    for item in itens:
        caminho_completo = os.path.join(caminho, item)
        if os.path.isdir(caminho_completo):
            pastas.append(item)
        else:
            arquivos.append(item)

    print(f"[Diretórios - {len(pastas)}]")
    for p in sorted(pastas):
        print(f"  [DIR]  {p}/")

    print(f"\n[Arquivos - {len(arquivos)}]")
    for a in sorted(arquivos):
        tam = os.path.getsize(os.path.join(caminho, a))
        print(f"  [ARQ]  {a} ({tam} bytes)")


if __name__ == "__main__":
    caminho_alvo = sys.argv[1] if len(sys.argv) > 1 else "."
    listar_diretorio(caminho_alvo)
