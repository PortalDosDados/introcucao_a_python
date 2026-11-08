"""
Exercício 10.6 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Altere a classe Conta de forma que ela possa receber uma lista de clientes,
permitindo a criação de contas conjuntas com múltiplos titulares.
"""


class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Conta:
    def __init__(self, clientes, numero, saldo=0):
        # Garante que clientes seja uma lista mesmo se passado um único cliente
        if isinstance(clientes, list):
            self.clientes = clientes
        else:
            self.clientes = [clientes]
        self.numero = numero
        self.saldo = saldo


if __name__ == "__main__":
    c1 = Cliente("João da Silva", "1111-2222")
    c2 = Cliente("Maria da Silva", "3333-4444")

    conta_conjunta = Conta(clientes=[c1, c2], numero="12345-6", saldo=1500.0)

    print(f"Conta Número: {conta_conjunta.numero}")
    print(f"Saldo: R$ {conta_conjunta.saldo:.2f}")
    print(f"Total de titulares: {len(conta_conjunta.clientes)}")
    for titular in conta_conjunta.clientes:
        print(f"  - Titular: {titular.nome} (Tel: {titular.telefone})")
