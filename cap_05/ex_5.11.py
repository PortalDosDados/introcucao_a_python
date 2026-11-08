"""
Exercício 5.11 Escreva um programa que pergunte o depósito inicial e a taxa de
juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros no período.
"""

deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (ex: 3 para 3%): "))

mes = 1
saldo = deposito

while mes <= 24:
    rendimento = saldo * (taxa / 100)
    saldo = saldo + rendimento
    print(f"Mês {mes:2d}: Saldo = R$ {saldo:10.2f}")
    mes = mes + 1

total_juros = saldo - deposito
print(f"Total ganho com juros: R$ {total_juros:.2f}")
