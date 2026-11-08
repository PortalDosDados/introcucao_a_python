"""
Exercício 5.20 O que acontece se digitarmos 0.001 no programa anterior? Caso ele
não funcione, altere-o de forma a corrigir o problema.

Resposta:
Se digitarmos 0.001 (ou frações menores que a menor moeda existente de R$ 0,01),
o valor não pode ser pago exatamente com as moedas em circulação.
Se o programa não tiver uma condição de parada quando o valor a pagar for menor
do que a menor moeda disponível (1 centavo), o laço pode entrar em repetição infinita
tentando reduzir um valor menor que a menor cédula/moeda.

Correção:
Garantir que, após testar a menor moeda (1 centavo), o programa encerre e alerte
sobre qualquer valor residual indivisível.
"""

valor = float(input("Digite o valor a pagar: R$ "))
apagar = int(round(valor * 100))
cedulas = 0
atual = 10000  # R$ 100,00

while True:
    if atual <= apagar:
        apagar = apagar - atual
        cedulas = cedulas + 1
    else:
        if cedulas > 0:
            if atual >= 100:
                print(f"{cedulas} cédula(s) de R$ {atual // 100}")
            else:
                print(f"{cedulas} moeda(s) de R$ {atual / 100:.2f}")

        if apagar == 0:
            break

        if atual == 10000:
            atual = 5000
        elif atual == 5000:
            atual = 2000
        elif atual == 2000:
            atual = 1000
        elif atual == 1000:
            atual = 500
        elif atual == 500:
            atual = 100
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        elif atual == 1:
            # Não existem moedas menores que 1 centavo
            if apagar > 0:
                print(f"Resto não pagável em moedas: R$ {apagar / 100:.3f}")
            break
        cedulas = 0
