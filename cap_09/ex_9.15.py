"""
Exercício 9.15 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Altere o jogo da forca para ler a lista de palavras a partir de um arquivo
externo ('palavras.txt'). Caso o arquivo não exista, crie-o com um conjunto
padrão de palavras.
"""

import os
import random

ARQUIVO_PALAVRAS_PADRAO = "palavras.txt"
PALAVRAS_INICIAIS = [
    "python",
    "programacao",
    "desenvolvimento",
    "computador",
    "arquivo",
    "algoritmo",
]


def carregar_ou_criar_palavras(caminho_arquivo=ARQUIVO_PALAVRAS_PADRAO):
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            for p in PALAVRAS_INICIAIS:
                f.write(f"{p}\n")

    palavras = []
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            item = linha.strip().lower()
            if item:
                palavras.append(item)
    return palavras


def jogar_forca_com_arquivo(caminho_arquivo=ARQUIVO_PALAVRAS_PADRAO, palpites=None):
    palavras = carregar_ou_criar_palavras(caminho_arquivo)
    palavra_secreta = random.choice(palavras)
    acertos = set()
    erros = 0
    max_erros = 6

    simulador = iter(palpites) if palpites is not None else None
    print(
        f"Palavra sorteada do arquivo '{caminho_arquivo}' ({len(palavras)} disponíveis)."
    )

    while erros < max_erros:
        painel = " ".join([l if l in acertos else "_" for l in palavra_secreta])
        print(f"Palavra: {painel} | Erros: {erros}/{max_erros}")

        if all(l in acertos for l in palavra_secreta):
            print(f"Parabéns! Você adivinhou a palavra: '{palavra_secreta}'!")
            return True

        if simulador is not None:
            try:
                chute = next(simulador).lower().strip()
                print(f"Palpite: {chute}")
            except StopIteration:
                break
        else:
            chute = input("Digite uma letra: ").lower().strip()

        if len(chute) != 1 or not chute.isalpha():
            continue

        if chute in palavra_secreta:
            acertos.add(chute)
        else:
            erros += 1

    return False


if __name__ == "__main__":
    arq_demo = "temp_palavras_demo.txt"
    with open(arq_demo, "w", encoding="utf-8") as f:
        f.write("python\n")

    jogar_forca_com_arquivo(arq_demo, palpites=["p", "y", "t", "h", "o", "n"])

    if os.path.exists(arq_demo):
        os.remove(arq_demo)
