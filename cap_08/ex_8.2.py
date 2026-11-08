"""
Exercício 8.2 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Escreva uma função que receba dois números e retorne True se o primeiro número
for múltiplo do segundo.
Valores esperados:
multiplo(8, 4) == True
multiplo(7, 3) == False
multiplo(5, 5) == True
"""


def multiplo(a, b):
    if b == 0:
        return False
    return a % b == 0


# Demonstração e testes
if __name__ == "__main__":
    print(f"multiplo(8, 4) = {multiplo(8, 4)}")
    print(f"multiplo(7, 3) = {multiplo(7, 3)}")
    print(f"multiplo(5, 5) = {multiplo(5, 5)}")
