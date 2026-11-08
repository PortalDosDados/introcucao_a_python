"""
Exercício 8.6 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Reescreva o Programa 8.2 de forma a utilizar for em vez de while para calcular
a soma dos elementos de uma lista.
"""


def soma(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total


# Demonstração e testes
if __name__ == "__main__":
    dados = [1, 7, 2, 9, 15]
    print(f"Lista: {dados}")
    print(f"Soma calculada: {soma(dados)}")
