"""
Exercício 7.10 Escreva um jogo da velha para dois jogadores. O jogo deve
perguntar onde você quer jogar e alternar entre os jogadores. A cada jogada,
verifique se a posição está livre. Verifique também quando um jogador venceu
a partida ou se houve empate.
"""

# Tabuleiro 3x3 inicializado com espaços vazios
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

jogador_atual = "X"
jogadas = 0

while True:
    # Exibe o tabuleiro
    print("\n   1   2   3")
    print(f"1  {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}")
    print("  ---+---+---")
    print(f"2  {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}")
    print("  ---+---+---")
    print(f"3  {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]}")

    # Entrada das coordenadas
    print(f"\nVez do jogador '{jogador_atual}'")
    linha = int(input("Digite a linha (1-3): ")) - 1
    coluna = int(input("Digite a coluna (1-3): ")) - 1

    # Validação de limites
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        print("Coordenadas inválidas! Escolha valores entre 1 e 3.")
        continue

    # Validação de posição livre
    if tabuleiro[linha][coluna] != " ":
        print("Esta posição já está ocupada! Escolha outra.")
        continue

    # Realiza a jogada
    tabuleiro[linha][coluna] = jogador_atual
    jogadas += 1

    # Verificação de vitória (linhas, colunas e diagonais)
    venceu = False

    # Linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador_atual:
            venceu = True

    # Colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador_atual:
            venceu = True

    # Diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador_atual:
        venceu = True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador_atual:
        venceu = True

    if venceu:
        print("\n   1   2   3")
        print(f"1  {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}")
        print("  ---+---+---")
        print(f"2  {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}")
        print("  ---+---+---")
        print(f"3  {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]}")
        print(f"\nParabéns! O jogador '{jogador_atual}' venceu a partida!")
        break

    if jogadas == 9:
        print("\nEmpate! Deu velha!")
        break

    # Alterna o jogador
    jogador_atual = "O" if jogador_atual == "X" else "X"
