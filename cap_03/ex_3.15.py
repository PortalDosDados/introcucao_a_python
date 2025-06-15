'''
Exercício 3.15

Escreva um programa para calcular a redução do tempo de vida de
um fumante. 

Pergunte a quantidade de cigarros fumados por dia e quantos anos
ele já fumou. 

Considere que um fumante perde 10 minutos de vida a cada cigarro,
calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

'''
temp_vida_perd_min = 10

cigarros_dia = int(input('Quantos cigarros você fuma por dia? '))
anos_fumando = int(input('Quantos anos você já fumou? '))

dias_por_ano = 365

anos_em_dias = anos_fumando * dias_por_ano

total_cigarros = cigarros_dia *anos_em_dias

total_minutos_perdidos = int(total_cigarros * 10)

total_dias_perdidos = int(total_minutos_perdidos / (24*60))

print(f'Você perdeu {total_dias_perdidos} dias da sua vida')