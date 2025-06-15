'''
Faça um programa que solicite o preço de uma mercadoria e o percentual 
de desconto.  Exiba o valor do desconto e o preço a pagar
'''
preco_mercadoria = float(input('Qual o valor da mercadoria? '))
percentual_desconto = float(input('Qual o percentual de desconto? '))
desconto = preco_mercadoria * (percentual_desconto / 100)
preco_com_desconto = preco_mercadoria *(1 - percentual_desconto/100)

print(f'Seu desconto foi {desconto}% O valor com desconto é R$ {preco_com_desconto:.2f}')

