"""
Exercício 6.1 Modifique o Programa 6.2 para ler 7 notas em vez de 5.
"""

notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0

while x < 7:
    notas[x] = float(input(f"Nota {x + 1}: "))
    soma = soma + notas[x]
    x = x + 1

x = 0
while x < 7:
    print(f"Nota {x + 1}: {notas[x]:6.2f}")
    x = x + 1

print(f"Média: {soma / x:6.2f}")
