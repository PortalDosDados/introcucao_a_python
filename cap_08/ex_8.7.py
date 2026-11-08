"""
Exercício 8.7 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Defina uma função recursiva que calcule o maior divisor comum (MDC) entre dois
números inteiros a e b maiores que zero:
- mdc(a, b) = a, se b == 0
- mdc(a, b) = mdc(b, a % b), se b > 0
(Algoritmo de Euclides)
"""


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


# Demonstração e testes
if __name__ == "__main__":
    print(f"mdc(10, 5) = {mdc(10, 5)}")
    print(f"mdc(32, 24) = {mdc(32, 24)}")
    print(f"mdc(54, 24) = {mdc(54, 24)}")
