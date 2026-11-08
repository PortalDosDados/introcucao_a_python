"""
Exercício 10.7 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Modifique o método resumo da classe Conta para exibir o nome e o telefone
de todos os clientes vinculados à conta conjunta.
"""


class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Conta:
    def __init__(self, clientes, numero, saldo=0):
        if isinstance(clientes, list):
            self.clientes = clientes
        else:
            self.clientes = [clientes]
        self.numero = numero
        self.saldo = saldo
        self.operacoes = []

    def resumo(self):
        print(f"\n{'=' * 40}")
        print(f"Resumo da Conta Número: {self.numero}")
        print(f"Saldo Atual: R$ {self.saldo:.2f}")
        print("Titulares:")
        for idx, c in enumerate(self.clientes, start=1):
            print(f"  {idx}. {c.nome} - Tel: {c.telefone}")
        print(f"{'=' * 40}")


if __name__ == "__main__":
    c1 = Cliente("Pedro Álvares", "9988-7766")
    c2 = Cliente("Isabela Álvares", "9988-5544")

    conta = Conta(clientes=[c1, c2], numero="99887-1", saldo=2540.50)
    conta.resumo()
