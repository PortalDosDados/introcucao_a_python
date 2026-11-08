"""
Exercício 8.8 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Usando a função mdc definida no exercício anterior, defina uma função para calcular
o menor múltiplo comum (MMC) entre dois números:
mmc(a, b) = (|a x b|) / mdc(a, b)
"""


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


def mmc(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // mdc(a, b)


# Demonstração e testes
if __name__ == "__main__":
    print(f"mmc(10, 5) = {mmc(10, 5)}")
    print(f"mmc(32, 24) = {mmc(32, 24)}")
    print(f"mmc(5, 3) = {mmc(5, 3)}")
