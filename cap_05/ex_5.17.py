"""
Exercício 5.17 O que acontece se digitarmos 0 (zero) no valor a pagar do Programa 5.1?

Resposta:
No Programa 5.1 original do livro, se o valor for 0:
1. `atual` inicia em 50 e `apagar` inicia em 0.
2. Como `atual <= apagar` (50 <= 0) é falso, o fluxo vai direto para o bloco `else`.
3. O programa imprime "0 cédula(s) de R$50".
4. A condição `if apagar == 0:` é verdadeira, acionando o `break` e finalizando o programa.

Portanto, o programa original imprime "0 cédula(s) de R$50" e para.
Abaixo está o código com o teste demonstrando esse comportamento.
"""

valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50
apagar = valor

while True:
    if atual <= apagar:
        apagar = apagar - atual
        cedulas = cedulas + 1
    else:
        print(f"{cedulas} cédula(s) de R$ {atual}")
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
