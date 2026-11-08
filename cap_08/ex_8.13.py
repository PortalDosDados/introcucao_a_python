"""
Exercício 8.13 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Altere o Programa 7.2 (jogo da forca) de forma a modularizá-lo em funções.
A palavra secreta deve ser sorteada aleatoriamente a partir de uma lista de
palavras utilizando a biblioteca random (random.choice).
"""

import random

PALAVRAS_PADRAO = [
    "python",
    "programacao",
    "algoritmo",
    "computador",
    "funcao",
    "variavel",
    "desenvolvimento",
]

LINHAS_FORCA = [
    "X==:==\nX  :  ",
    "X  O  ",
    "X \\|  ",
    "X \\|/ ",
    "X /   ",
    "X / \\ ",
]


def sortear_palavra(lista_palavras):
    return random.choice(lista_palavras).lower()


def desenhar_forca(erros):
    print("X==:==")
    print("X  :  ")
    if erros >= 1:
        print("X  O  ")
    else:
        print("X")

    if erros == 2:
        print("X  |  ")
    elif erros == 3:
        print("X \\|  ")
    elif erros >= 4:
        print("X \\|/ ")
    else:
        print("X")

    if erros == 5:
        print("X /   ")
    elif erros >= 6:
        print("X / \\ ")
    else:
        print("X")
    print("X\n===========")


def exibir_painel(palavra_secreta, acertos):
    painel = ""
    for letra in palavra_secreta:
        painel += f"{letra} " if letra in acertos else "_ "
    return painel.strip()


def jogar(lista_palavras=None, max_erros=6, palpites_simulados=None):
    if lista_palavras is None:
        lista_palavras = PALAVRAS_PADRAO

    palavra_secreta = sortear_palavra(lista_palavras)
    acertos = set()
    erros = 0
    letras_tentadas = set()

    simulador = iter(palpites_simulados) if palpites_simulados is not None else None

    print("\n=== Jogo da Forca com Funções ===")

    while True:
        desenhar_forca(erros)
        painel = exibir_painel(palavra_secreta, acertos)
        print(f"Palavra: {painel}")
        print(f"Erros: {erros}/{max_erros}")

        if all(letra in acertos for letra in palavra_secreta):
            print("\nParabéns! Você venceu!")
            return True

        if erros >= max_erros:
            print(f"\nVocê foi enforcado! A palavra era: {palavra_secreta}")
            return False

        if simulador is not None:
            try:
                chute = next(simulador).lower().strip()
                print(f"Palpite (simulado): {chute}")
            except StopIteration:
                print("Fim das entradas de teste.")
                break
        else:
            chute = input("Digite uma letra: ").lower().strip()

        if len(chute) != 1 or not chute.isalpha():
            print("Digite apenas uma única letra válida.")
            continue

        if chute in letras_tentadas:
            print("Você já tentou essa letra!")
            continue

        letras_tentadas.add(chute)

        if chute in palavra_secreta:
            acertos.add(chute)
            print(f"Boa! A letra '{chute}' existe na palavra.")
        else:
            erros += 1
            print(f"Que pena! A letra '{chute}' não existe na palavra.")


if __name__ == "__main__":
    # Demonstração não-interativa simulada
    print("Executando rodada simulada do jogo:")
    jogar(
        lista_palavras=["python"],
        max_erros=6,
        palpites_simulados=["a", "p", "y", "t", "h", "o", "n"],
    )
