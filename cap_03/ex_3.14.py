'''
Exercício 3.14 

Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
dia e R$ 0,15 por km rodado.

'''

custo_carro_dia = 60
custo_km_rodado = 0.15


dias_alugado = int(input('Por quantos dias você alugou o carro? '))
kms_rodados = float(input('Quantos Kms você rodou? '))

total_a_pagar = (dias_alugado * custo_carro_dia) + (kms_rodados * custo_km_rodado)

print(f'Você deve pagar R$ {total_a_pagar}')