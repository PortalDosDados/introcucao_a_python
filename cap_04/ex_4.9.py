'''

Exercício 4.9 

Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
casa a comprar dividido pelo número de meses a pagar.

'''
print('Olá, seja bem vindo!')

print('Gostaria de comprar uma casa? Vou precisar de algumas informações.')

valor_casa = float(input('Qual valor da casa que você pretende comprar? '))

renda = float(input('Qual sua renda atual? '))

qtd_parcelas_anos = int(input('Em quantos anos você gostaria de pagar? '))

qtd_parcelas_meses = qtd_parcelas_anos / 12

valor_prestação = valor_casa / qtd_parcelas_meses

if valor_prestação > renda*0.3:
    print(f'A parcela fica R${valor_prestação:.2f}, esse valor é maior do que 30% da sua renda')
    print('Emprestimo negado')
else:
    print(f'Emprestimo concedido, sua parcela será R${valor_prestação:.2f}')