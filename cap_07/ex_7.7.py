"""
Exercício 7.7 Modifique o jogo da forca (Programa 7.2) de forma a escrever
a palavra secreta caso o jogador perca.
"""

palavra = input("Digite a palavra secreta: ").lower().strip()

for x in range(50):
    print()  # Limpa a tela visualmente

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
