"""
Exercício 8.15 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Desenvolva uma função recursiva que receba uma lista que pode conter outras listas
(a qualquer nível de aninhamento) e imprima todos os elementos da lista,
exibindo a estrutura hierárquica por meio de recuos proporcionais ao nível de
profundidade de cada sublista.
"""


def imprime_elementos(lista, nivel=0):
    espaco = "  " * nivel
    for item in lista:
        if isinstance(item, list):
            print(f"{espaco}[Sublista nível {nivel + 1}]:")
            imprime_elementos(item, nivel + 1)
        else:
            print(f"{espaco}- {item}")


def achatar_lista(lista):
    """Retorna uma nova lista unidimensional (flat) com todos os elementos."""
    resultado = []
    for item in lista:
        if isinstance(item, list):
            resultado.extend(achatar_lista(item))
        else:
            resultado.append(item)
    return resultado


# Demonstração e testes
if __name__ == "__main__":
    lista_aninhada = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]

    print("Lista original aninhada:")
    print(lista_aninhada)

    print("\nImpressão hierárquica recursiva:")
    imprime_elementos(lista_aninhada)

    print("\nLista achatada (unidimensional):")
    print(achatar_lista(lista_aninhada))
