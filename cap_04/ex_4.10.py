'''
Exercício 4.10 Escreva um programa que calcule o preço a pagar pelo fornecimento
de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação:
R para residências, I para indústrias e C para comércios. Calcule o preço a
pagar de acordo com a tabela a seguir.


'''

# Dicionário com as tarifas por tipo de instalação e faixa de consumo
tarifas = {
    "Residencial": [
        {"faixa": (0, 500), "preco": 0.40},
        {"faixa": (501, float('inf')), "preco": 0.65}
    ],
    "Comercial": [
        {"faixa": (0, 1000), "preco": 0.55},
        {"faixa": (1001, float('inf')), "preco": 0.60}
    ],
    "Industrial": [
        {"faixa": (0, 5000), "preco": 0.55},
        {"faixa": (5001, float('inf')), "preco": 0.60}
    ]
}

# Saudação inicial
print('Seja bem-vindo!')

# Entrada do consumo (convertida para float)
kWh_consumida = float(input('Quantos KWh você consumiu nesse mês? '))

# Entrada do tipo de instalação (em maiúsculo)
tipo_de_instalacao = input('Qual o tipo da sua instalação?\n R = Residencial\n I = Industrial\n C = Comercial\n\nResposta: ').upper()

# Determina o tipo de instalação com base na entrada
if tipo_de_instalacao == 'R':
    tp_inst = 'Residencial'
elif tipo_de_instalacao == 'I':
    tp_inst = 'Industrial'
elif tipo_de_instalacao == 'C':
    tp_inst = 'Comercial'
else:
    print("Tipo de instalação inválido.")
    exit()

# Busca o preço de acordo com a faixa correspondente
preco_final = 0
for faixa in tarifas[tp_inst]:
    if faixa["faixa"][0] <= kWh_consumida <= faixa["faixa"][1]:
        preco_final = faixa["preco"] * kWh_consumida
        break

# Resultado
print(f'\nTipo de instalação: {tp_inst}')
print(f'Consumo: {kWh_consumida:.2f} kWh')
print(f'Valor a pagar: R$ {preco_final:.2f}')
