'''
Exercício 4.4

Escreva um programa que pergunte o salário do funcionário e calcule
o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
10%. Para os inferiores ou iguais, de 15%.

'''

salario = float(input('Informe o salário do funcionário: R$ '))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

print(f'O aumento do salário é de R$ {aumento:.2f}, totalizando R$ {salario + aumento:.2f}.')