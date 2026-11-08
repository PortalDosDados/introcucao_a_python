"""
Exercício 5.27 Escreva um programa que verifique se um número é palíndromo.
Um número é palíndromo se continua o mesmo caso lido de trás para frente até a frente.
Exemplo: 454 ou 10501 são palíndromos.
"""

numero = int(input("Digite um número inteiro: "))

# Utilizando pura lógica de repetição matemática (sem manipulação avançada de strings):
# Invertemos o número extraindo o último dígito (% 10) e reduzindo o número (// 10).
original = numero
invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = (invertido * 10) + digito
    numero = numero // 10

if original == invertido:
    print(f"O número {original} é palíndromo!")
else:
    print(f"O número {original} NÃO é palíndromo (invertido fica {invertido}).")
