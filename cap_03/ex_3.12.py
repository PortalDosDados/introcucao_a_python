'''
Exercício 3.12 

Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
Exercício

'''

distancia = float(input('Qual a distância a percorrer em km? '))
velocidade = float(input('Qual a velocidade média esperada para a viagem em km/h? '))
tempo = distancia / velocidade
print(f'O tempo estimado para a viagem é de {tempo:.2f} horas.')
