'''
Exercício 3.13 

Escreva um programa que converta uma temperatura digitada em
°C em °F. A fórmula para essa conversão é:
F = ((9 x C) / 5) + 32

'''

temp_celsius = float(input('Digite a temperatura em °C: '))
temp_fahrenheit = ((9 * temp_celsius) / 5) + 32
print(f'A temperatura em °F é: {temp_fahrenheit:.2f}°F')

