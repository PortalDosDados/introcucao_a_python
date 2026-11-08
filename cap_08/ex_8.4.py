"""
Exercício 8.4 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Escreva uma função que receba a base e a altura de um triângulo e retorne sua área
(A = (base x altura) / 2).
Valores esperados:
area_triangulo(6, 9) == 27
area_triangulo(5, 8) == 20
"""


def area_triangulo(base, altura):
    return (base * altura) / 2


# Demonstração e testes
if __name__ == "__main__":
    print(f"area_triangulo(6, 9) = {area_triangulo(6, 9)}")
    print(f"area_triangulo(5, 8) = {area_triangulo(5, 8)}")
