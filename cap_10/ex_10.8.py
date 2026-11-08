"""
Exercício 10.8 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie a classe Cliente com os atributos nome e telefone. Adicione um método
especial __str__ para representação legível do cliente e validações nos atributos.
"""


class Cliente:
    def __init__(self, nome, telefone):
        if not nome:
            raise ValueError("O nome do cliente não pode ser vazio.")
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"Cliente(Nome: {self.nome}, Telefone: {self.telefone})"


if __name__ == "__main__":
    cliente_a = Cliente("Ana Beatriz", "98123-4567")
    cliente_b = Cliente("Roberto Carlos", "97654-3210")

    print(cliente_a)
    print(cliente_b)
