"""
Exercício 5.7 Modifique o programa anterior de forma que o usuário também
digite o início e o fim da tabuada, em vez de começar com 1 e 10.
"""

tabuada = int(input("Tabuada de: "))
inicio = int(input("De: "))
fim = int(input("Até: "))

x = inicio
while x <= fim:
    print(f"{tabuada} x {x} = {tabuada * x}")
    x = x + 1
