"""
Exercício 5.26 Escreva um programa que calcule o resto da divisão inteira entre
dois números. Utilize apenas as operações de soma e subtração para calcular o resultado.
"""

dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

if divisor == 0:
    print("Divisão por zero não é permitida.")
else:
    resto = dividendo
    while resto >= divisor:
        resto = resto - divisor

    print(f"O resto da divisão de {dividendo} por {divisor} é {resto}")
