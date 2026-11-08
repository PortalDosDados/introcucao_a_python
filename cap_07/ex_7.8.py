"""
Exercício 7.8 Modifique o jogo da forca de forma a utilizar uma lista de palavras.
No início, selecione uma palavra da lista.
"""

palavras = [
    "computador",
    "programacao",
    "python",
    "algoritmo",
    "teclado",
    "desenvolvimento",
    "variavel",
]

# Solicita um número ao jogador para selecionar a palavra da lista (sem depender de random do cap 8)
indice = (
    int(
        input(
            f"Digite um número de 1 a {len(palavras)} para escolher a palavra secreta: "
        )
    )
    - 1
)
palavra = palavras[indice % len(palavras)]

for x in range(50):
    print()

digitadas = []
acertos = []
erros = 0

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)

    if senha == palavra:
        print("Você acertou!")
        break

    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas.append(tentativa)
        if tentativa in palavra:
            acertos.append(tentativa)
        else:
            erros += 1
            print("Você errou!")

    print("X==:==\nX  :  ")
    print("X  O  " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " \|  "
    elif erros >= 4:
        linha2 = " \|/ "
    print(f"X{linha2}")
    linha3 = ""
    if erros == 5:
        linha3 = " /   "
    elif erros >= 6:
        linha3 = " / \ "
    print(f"X{linha3}")
    print("X\n=======")

    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break
