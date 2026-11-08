"""
Exercício 5.12 Altere o programa anterior de forma a perguntar também o valor
depositado mensalmente. Esse valor será depositado no início de cada mês, e você
deve considerá-lo para o cálculo de juros do mês seguinte.
"""

deposito_inicial = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (ex: 3 para 3%): "))
aporte_mensal = float(input("Depósito mensal: "))

mes = 1
saldo = deposito_inicial
total_investido = deposito_inicial

while mes <= 24:
    saldo = saldo + aporte_mensal
    rendimento = saldo * (taxa / 100)
    saldo = saldo + rendimento
    total_investido = total_investido + aporte_mensal
    print(f"Mês {mes:2d}: Saldo = R$ {saldo:10.2f}")
    mes = mes + 1

total_juros = saldo - total_investido
print(f"Total investido: R$ {total_investido:.2f}")
print(f"Total ganho com juros: R$ {total_juros:.2f}")
