"""
Exercício 8.10 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Reescreva a função para calcular a sequência de Fibonacci sem usar recursão
(forma iterativa).
"""


def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    anterior = 0
    atual = 1
    for _ in range(2, n + 1):
        anterior, atual = atual, anterior + atual
    return atual


# Demonstração e testes
if __name__ == "__main__":
    print("Primeiros 10 termos da sequência de Fibonacci (iterativo):")
    termos = [fibonacci(i) for i in range(10)]
    print(termos)
