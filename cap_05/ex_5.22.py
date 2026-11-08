"""
Exercício 5.22 Escreva um programa que exiba uma lista de opções (menu): adição,
subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
"""

while True:
    print("\n--- MENU DE OPERAÇÕES ---")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 5:
        print("Saindo do programa...")
        break

    if opcao < 1 or opcao > 5:
        print("Opção inválida! Tente novamente.")
        continue

    tabuada = int(input("Tabuada do número: "))
    numero = 1

    while numero <= 10:
        if opcao == 1:
            print(f"{tabuada} + {numero} = {tabuada + numero}")
        elif opcao == 2:
            print(f"{tabuada} - {numero} = {tabuada - numero}")
        elif opcao == 3:
            print(f"{tabuada} x {numero} = {tabuada * numero}")
        elif opcao == 4:
            print(f"{tabuada} / {numero} = {tabuada / numero:.2f}")
        numero = numero + 1
