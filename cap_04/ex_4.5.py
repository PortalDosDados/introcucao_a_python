num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

# Inicializa com o primeiro número
maior = num1
menor = num1

# Verifica o maior
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

# Verifica o menor
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f'O maior número é {maior} e o menor número é {menor}.')
