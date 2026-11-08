"""
Exercício 5.8 Escreva um programa que leia dois números. Imprima o resultado da
multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
subtração para calcular o resultado. Lembre-se de que podemos entender a
multiplicação de dois números como somas sucessivas de um deles.
"""

primeiro = int(input("Primeiro número: "))
segundo = int(input("Segundo número: "))

resultado = 0
x = 1
while x <= segundo:
    resultado = resultado + primeiro
    x = x + 1

print(f"{primeiro} x {segundo} = {resultado}")
