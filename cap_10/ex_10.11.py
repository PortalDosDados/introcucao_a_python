"""
Exercício 10.11 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Modifique a classe ContaEspecial para que seu método extrato exiba detalhadamente
todas as operações, o saldo atual, o limite de crédito e o saldo total disponível
para saque (saldo + limite).
"""


class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.clientes = clientes if isinstance(clientes, list) else [clientes]
        self.numero = numero
        self.saldo = saldo
        self.operacoes = []

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        print(f"Saldo insuficiente na conta {self.numero}.")
        return False

    def extrato(self):
        print(f"\nExtrato Conta Nº {self.numero}")
        for op, val in self.operacoes:
            print(f"  {op:10s}: R$ {val:10.2f}")
        print(f"  Saldo Atual: R$ {self.saldo:10.2f}")


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=500):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if (self.saldo + self.limite) >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        print(f"Saldo e limite insuficientes na conta especial {self.numero}.")
        return False

    def extrato(self):
        print(f"\n{'=' * 45}")
        print(f"Extrato Detalhado da Conta Especial Nº {self.numero}")
        print(f"{'=' * 45}")
        for op, val in self.operacoes:
            print(f"  {op:10s}: R$ {val:10.2f}")
        print(f"{'-' * 45}")
        print(f"  Saldo em Conta:  R$ {self.saldo:10.2f}")
        print(f"  Limite Cheque:   R$ {self.limite:10.2f}")
        disponivel = self.saldo + self.limite
        print(f"  Total Disponível: R$ {disponivel:10.2f}")
        print(f"{'=' * 45}")


if __name__ == "__main__":
    ce = ContaEspecial("Daniela", "3333-1", saldo=500.0, limite=1000.0)
    ce.deposito(200.0)
    ce.saque(900.0)
    ce.extrato()
