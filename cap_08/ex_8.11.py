"""
Exercício 8.11 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Escreva uma função para validar uma string. Essa função recebe como parâmetro
a string, o número mínimo e o número máximo de caracteres permitidos. Retorne
True se o tamanho da string estiver entre os valores mínimo e máximo (inclusive),
e False caso contrário.
"""


def valida_string(texto, minimo, maximo):
    tamanho = len(texto)
    return minimo <= tamanho <= maximo


# Demonstração e testes
if __name__ == "__main__":
    print(f"valida_string('Python', 1, 10): {valida_string('Python', 1, 10)}")
    print(f"valida_string('Python', 1, 4): {valida_string('Python', 1, 4)}")
    print(f"valida_string('', 1, 5): {valida_string('', 1, 5)}")
