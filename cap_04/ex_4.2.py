'''
Exercício 4.2 

Escreva um programa que pergunte a velocidade do carro de um
usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
80 km/h.

'''

velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 5
    print(f'O valor da multa é R$ {multa:.2f}')
    print('Dirija com cuidado!')
else:
    print('Você não foi multado!')