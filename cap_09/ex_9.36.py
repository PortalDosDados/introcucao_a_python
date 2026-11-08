"""
Exercício 9.36 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que receba o caminho de um diretório e exiba toda a sua
árvore hierárquica recursivamente (semelhante ao comando tree do sistema operacional).
"""

import os
import sys


def exibir_arvore_diretorios(diretorio=".", nivel=0, prefixo=""):
    if not os.path.exists(diretorio):
        print(f"Erro: Caminho '{diretorio}' não encontrado.")
        return

    if nivel == 0:
        print(f"\n[Raiz] {os.path.abspath(diretorio)}")

    try:
        itens = sorted(os.listdir(diretorio))
    except PermissionError:
        print(f"{prefixo}\\-- [Acesso Negado]")
        return

    total = len(itens)
    for idx, item in enumerate(itens):
        caminho_completo = os.path.join(diretorio, item)
        eh_ultimo = idx == total - 1
        marcador = "\\-- " if eh_ultimo else "|-- "
        extensao_prefixo = "    " if eh_ultimo else "|   "

        if os.path.isdir(caminho_completo):
            print(f"{prefixo}{marcador}[DIR] {item}/")
            exibir_arvore_diretorios(
                caminho_completo, nivel + 1, prefixo + extensao_prefixo
            )
        else:
            tamanho = os.path.getsize(caminho_completo)
            print(f"{prefixo}{marcador}{item} ({tamanho} bytes)")


if __name__ == "__main__":
    caminho_alvo = sys.argv[1] if len(sys.argv) > 1 else "."
    # Limita a profundidade ou testa pasta de teste para execução autônoma rápida
    pasta_teste = "temp_teste_tree"
    if len(sys.argv) == 1:
        os.makedirs(os.path.join(pasta_teste, "sub1"), exist_ok=True)
        os.makedirs(os.path.join(pasta_teste, "sub2"), exist_ok=True)
        with open(os.path.join(pasta_teste, "arquivo1.txt"), "w") as f:
            f.write("a")
        with open(os.path.join(pasta_teste, "sub1", "arquivo2.txt"), "w") as f:
            f.write("b")

        exibir_arvore_diretorios(pasta_teste)

        # Limpeza
        os.remove(os.path.join(pasta_teste, "arquivo1.txt"))
        os.remove(os.path.join(pasta_teste, "sub1", "arquivo2.txt"))
        os.rmdir(os.path.join(pasta_teste, "sub1"))
        os.rmdir(os.path.join(pasta_teste, "sub2"))
        os.rmdir(pasta_teste)
    else:
        exibir_arvore_diretorios(caminho_alvo)
