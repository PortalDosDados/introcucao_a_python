"""
Exercício 6.13 A lista de temperaturas de Mons, na Bélgica, foi armazenada em:
T = [-10, -8, 0, 1, 2, 5, -2, -4]
Faça um programa que imprima a menor e a maior temperatura, assim como a
temperatura média.
"""

t = [-10, -8, 0, 1, 2, 5, -2, -4]

menor = t[0]
maior = t[0]
soma = 0

for temp in t:
    if temp < menor:
        menor = temp
    if temp > maior:
        maior = temp
    soma = soma + temp

media = soma / len(t)

print(f"Temperaturas registradas: {t}")
print(f"Menor temperatura: {menor} °C")
print(f"Maior temperatura: {maior} °C")
print(f"Temperatura média: {media:.2f} °C")
