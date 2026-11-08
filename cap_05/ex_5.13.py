"""
Exercício 5.13 Escreva um programa que pergunte o valor inicial de uma dívida e
o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de
meses para que a dívida seja paga, o total pago e o total de juros pago.
"""

divida_inicial = float(input("Valor inicial da dívida: R$ "))
taxa = float(input("Juros mensal (em %): "))
pagamento_mensal = float(input("Pagamento mensal: R$ "))

# Validação para evitar laço infinito caso o pagamento não cubra os juros do primeiro mês
juros_primeiro_mes = divida_inicial * (taxa / 100)
if pagamento_mensal <= juros_primeiro_mes:
    print(
        "O pagamento mensal é menor ou igual aos juros mensais. A dívida nunca será paga."
    )
else:
    mes = 0
    divida = divida_inicial
    total_pago = 0.0

    while divida > 0:
        juros = divida * (taxa / 100)
        divida = divida + juros
        mes = mes + 1

        if divida >= pagamento_mensal:
            pago_neste_mes = pagamento_mensal
            divida = divida - pagamento_mensal
        else:
            pago_neste_mes = divida
            divida = 0.0

        total_pago = total_pago + pago_neste_mes

    total_juros = total_pago - divida_inicial
    print(f"Para pagar a dívida serão necessários {mes} meses.")
    print(f"Total pago: R$ {total_pago:.2f}")
    print(f"Total de juros pago: R$ {total_juros:.2f}")
