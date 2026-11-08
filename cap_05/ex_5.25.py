"""
Exercício 5.25 Escreva um programa que calcule a raiz quadrada de um número.
Utilize o método de Newton para obter um resultado aproximado. Sendo n o número
a obter a raiz quadrada, considere a base b=2. Calcule p=(b+(n/b))/2. Agora,
calcule o quadrado de p. A cada passo, faça b=p e recalcule p usando a mesma
fórmula até que a diferença absoluta entre n e o quadrado de p seja menor que 0,0001.
"""

n = float(input("Digite um número para calcular a raiz quadrada: "))

if n < 0:
    print(
        "Não é possível calcular a raiz quadrada de número negativo com números reais."
    )
elif n == 0:
    print("A raiz quadrada de 0 é 0.0")
else:
    b = 2.0
    p = (b + (n / b)) / 2.0

    while abs(n - (p**2)) >= 0.0001:
        b = p
        p = (b + (n / b)) / 2.0

    print(f"A raiz quadrada aproximada de {n} é {p:.4f}")
