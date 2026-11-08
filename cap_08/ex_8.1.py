"""
Exercício 8.1 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Escreva uma função que retorne o maior de dois números.
Valores esperados:
maximo(5, 6) == 6
maximo(2, 1) == 2
maximo(7, 7) == 7
"""


def maximo(a, b):
    if a > b:
        return a
    return b


# Demonstração e testes
if __name__ == "__main__":
    print(f"maximo(5, 6) = {maximo(5, 6)}")
    print(f"maximo(2, 1) = {maximo(2, 1)}")
    print(f"maximo(7, 7) = {maximo(7, 7)}")
