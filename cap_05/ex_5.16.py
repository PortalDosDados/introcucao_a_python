"""
Exercício 5.16 Execute o Programa 5.1 para os seguintes valores: 501, 745, 384, 1126 e 2.
"""

valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50
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
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
