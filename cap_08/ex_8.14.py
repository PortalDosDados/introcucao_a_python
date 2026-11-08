"""
Exercício 8.14 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Altere o jogo da forca com funções de forma a escolher a palavra secreta com
base no nível de dificuldade escolhido pelo usuário:
- Fácil: palavras com até 5 letras
- Médio: palavras com 6 a 8 letras
- Difícil: palavras com mais de 8 letras
"""

import random

BANCO_DE_PALAVRAS = {
    "facil": ["casa", "sol", "lua", "gato", "livro", "cafe"],
    "medio": ["janela", "codigo", "python", "teclado", "floresta"],
    "dificil": ["algoritmo", "programador", "arquitetura", "desenvolvimento"],
}


def sortear_palavra_por_dificuldade(dificuldade):
    dificuldade = dificuldade.lower().strip()
    if dificuldade not in BANCO_DE_PALAVRAS:
        dificuldade = "medio"
    return random.choice(BANCO_DE_PALAVRAS[dificuldade])


def exibir_painel(palavra_secreta, acertos):
    painel = ""
    for letra in palavra_secreta:
        painel += f"{letra} " if letra in acertos else "_ "
    return painel.strip()


def jogar_forca(dificuldade="facil", palpites_simulados=None):
    palavra_secreta = sortear_palavra_por_dificuldade(dificuldade)
    max_erros = 6
    erros = 0
    acertos = set()
    letras_tentadas = set()

    simulador = iter(palpites_simulados) if palpites_simulados is not None else None

    print(f"\nIniciando Jogo da Forca - Nível: {dificuldade.upper()}")

    while erros < max_erros:
        painel = exibir_painel(palavra_secreta, acertos)
        print(f"Palavra: {painel} | Erros: {erros}/{max_erros}")

        if all(letra in acertos for letra in palavra_secreta):
            print(f"Parabéns! Você descobriu a palavra: '{palavra_secreta}'!")
            return True

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
            print("Letra já tentada anteriormente.")
            continue

        letras_tentadas.add(chute)

        if chute in palavra_secreta:
            acertos.add(chute)
            print(f"Letra '{chute}' encontrada!")
        else:
            erros += 1
            print(f"Letra '{chute}' incorreta!")

    if erros >= max_erros:
        print(f"Você perdeu! A palavra secreta era: '{palavra_secreta}'.")
        return False


if __name__ == "__main__":
    # Teste simulado para validação
    print("Teste com nível 'facil':")
    jogar_forca(dificuldade="facil", palpites_simulados=["a", "e", "i", "o", "u"])
