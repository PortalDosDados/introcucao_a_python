"""
Exercício 8.5 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Reescreva a função do Programa 8.1 de forma a utilizar a instrução for ou o
operador in para pesquisar um elemento em uma lista, retornando o seu índice
caso encontrado, ou None se o valor não estiver na lista.
"""


def pesquise(lista, valor):
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return i
    return None


# Demonstração e testes
if __name__ == "__main__":
    lista_exemplo = [10, 20, 30, 40, 50]
    print(f"Lista: {lista_exemplo}")
    print(f"pesquise(lista, 30): {pesquise(lista_exemplo, 30)}")
    print(f"pesquise(lista, 99): {pesquise(lista_exemplo, 99)}")
