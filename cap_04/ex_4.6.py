'''
Exercício 4.6 

Escreva um programa que pergunte a distância que um passageiro
deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.


'''

distancia = float(input('Digite a distância da viagem em km: '))
if distancia <= 200:
    preco_do_km = distancia * 0.50
else:
    preco_do_km = distancia * 0.45

print(f'O preço da passagem é R$ {preco_do_km:.2f}.')