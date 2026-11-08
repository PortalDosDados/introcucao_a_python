"""
Exercício 7.9 Modifique o jogo da forca para escrever mais detalhes do corpo
a cada erro: cabeça (1), tronco (2), braço esquerdo (3), braço direito (4),
perna esquerda (5) e perna direita (6).
"""

palavras = ["abacaxi", "morango", "laranja", "melancia", "uva", "banana"]
indice = int(input(f"Escolha um número de 1 a {len(palavras)}: ")) - 1
palavra = palavras[indice % len(palavras)]

for _ in range(50):
    print()

digitadas = []
acertos = []
erros = 0

# Gráficos da forca para cada quantidade de erros (0 a 6)
desenho = [
    "X==:==\nX  :  \nX     \nX     \nX     \nX\n=======",
    "X==:==\nX  :  \nX  O  \nX     \nX     \nX\n=======",
    "X==:==\nX  :  \nX  O  \nX  |  \nX     \nX\n=======",
    "X==:==\nX  :  \nX  O  \nX /|  \nX     \nX\n=======",
    "X==:==\nX  :  \nX  O  \nX /|\ \nX     \nX\n=======",
    "X==:==\nX  :  \nX  O  \nX /|\ \nX /   \nX\n=======",
    "X==:==\nX  :  \nX  O  \nX /|\ \nX / \ \nX\n=======",
]

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "_"
    print(f"Palavra: {' '.join(senha)}")
    print(f"Letras já tentadas: {', '.join(digitadas)}")

    if "_" not in senha:
        print("\nParabéns! Você venceu!")
        break

    tentativa = input("\nDigite uma letra: ").lower().strip()
    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Digite apenas uma letra válida!")
        continue

    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue

    digitadas.append(tentativa)

    if tentativa in palavra:
        acertos.append(tentativa)
        print("Letra correta!")
    else:
        erros += 1
        print("Letra incorreta!")

    print(desenho[erros])

    if erros == 6:
        print("\nEnforcado! Você perdeu!")
        print(f"A palavra secreta era: {palavra}")
        break
