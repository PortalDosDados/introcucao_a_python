"""
Exercício 5.18 Modifique o Programa 5.1 para também trabalhar com notas de R$ 100.
"""

valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100
apagar = valor

while True:
    if atual <= apagar:
        apagar = apagar - atual
        cedulas = cedulas + 1
    else:
        if cedulas > 0:
            print(f"{cedulas} cédula(s) de R$ {atual}")
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
