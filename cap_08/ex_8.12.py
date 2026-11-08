"""
Exercício 8.12 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Escreva uma função que receba uma string e uma lista de opções válidas.
A função deve comparar a string com os elementos da lista e retornar True se a
string for encontrada dentro da lista, e False caso contrário.
"""


def valida_opcao(texto, opcoes):
    return texto in opcoes


# Demonstração e testes
if __name__ == "__main__":
    frutas = ["maca", "banana", "pera", "laranja"]
    print(f"Lista de opcoes: {frutas}")
    print(f"valida_opcao('banana', frutas): {valida_opcao('banana', frutas)}")
    print(f"valida_opcao('uva', frutas): {valida_opcao('uva', frutas)}")
