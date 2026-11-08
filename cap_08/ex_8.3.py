"""
Exercício 8.3 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Escreva uma função que receba o lado de um quadrado e retorne sua área (A = lado²).
Valores esperados:
area_quadrado(4) == 16
area_quadrado(9) == 81
"""


def area_quadrado(lado):
    return lado**2


# Demonstração e testes
if __name__ == "__main__":
    print(f"area_quadrado(4) = {area_quadrado(4)}")
    print(f"area_quadrado(9) = {area_quadrado(9)}")
