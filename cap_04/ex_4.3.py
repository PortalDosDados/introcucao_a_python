'''
Exercício 4.3 

Escreva um programa que leia três números e que imprima o maior
e o menor.

'''

num_01 = int(input('Digite um dúmero: '))
num_02 = int(input('Digite outro número: '))
num_03 = int(input('Digite mais um número: '))



# Alternativa usando condicionais aninhados

if num_01 > num_02 and num_01 > num_03:
    maior = num_01
elif num_02 > num_01 and num_02 > num_03:
    maior = num_02
else:
    maior = num_03  
if num_01 < num_02 and num_01 < num_03:
    menor = num_01
elif num_02 < num_01 and num_02 < num_03:
    menor = num_02
else:
    menor = num_03
print(f'O maior número é {maior} e o menor é {menor}.')



# Alternativa usando a função max() e min()

maior = max(num_01, num_02, num_03)
menor = min(num_01, num_02, num_03)
print(f'O maior número é {maior} e o menor é {menor}.')