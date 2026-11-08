"""
Exercício 6.12 Altere o Programa 6.11 de forma a imprimir o menor elemento da lista.
"""

l = [12, 7, 9, 3, 10, 15]
menor = l[0]

for elemento in l:
    if elemento < menor:
        menor = elemento

print(f"Lista: {l}")
print(f"O menor elemento da lista é: {menor}")
