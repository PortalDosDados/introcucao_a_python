"""
Exercício 5.19 Modifique o Programa 5.1 para aceitar valores decimais, ou seja,
também contar moedas de 0.01, 0.02, 0.05, 0.10 e 0.50.
"""

# Trabalhamos com valores em centavos (inteiros) para evitar erros de precisão do ponto flutuante
valor = float(input("Digite o valor a pagar: R$ "))
apagar = int(round(valor * 100))
cedulas = 0
atual = 10000  # R$ 100,00

while True:
    if atual <= apagar:
        apagar = apagar - atual
        cedulas = cedulas + 1
    else:
        if cedulas > 0:
            if atual >= 100:
                print(f"{cedulas} cédula(s) de R$ {atual // 100}")
            else:
                print(f"{cedulas} moeda(s) de R$ {atual / 100:.2f}")

        if apagar == 0:
            break

        if atual == 10000:
            atual = 5000  # R$ 50,00
        elif atual == 5000:
            atual = 2000  # R$ 20,00
        elif atual == 2000:
            atual = 1000  # R$ 10,00
        elif atual == 1000:
            atual = 500  # R$ 5,00
        elif atual == 500:
            atual = 100  # R$ 1,00
        elif atual == 100:
            atual = 50  # R$ 0,50
        elif atual == 50:
            atual = 20  # R$ 0,20
        elif atual == 20:
            atual = 10  # R$ 0,10
        elif atual == 10:
            atual = 5  # R$ 0,05
        elif atual == 5:
            atual = 2  # R$ 0,02
        elif atual == 2:
            atual = 1  # R$ 0,01
        cedulas = 0
