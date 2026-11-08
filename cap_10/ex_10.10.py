"""
Exercício 10.10 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie a classe Conta e a subclasse ContaEspecial que herda de Conta.
A classe ContaEspecial deve ter um atributo adicional limite e sobrescrever
o método saque para permitir que o saldo fique negativo até o limite contratado.
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
        else:
            print(f"Saldo insuficiente na conta {self.numero}.")
            return False


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=500):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if (self.saldo + self.limite) >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        else:
            print(f"Saldo e limite insuficientes na conta especial {self.numero}.")
            return False


if __name__ == "__main__":
    conta_comum = Conta("Lucas", "1001", saldo=200)
    conta_especial = ContaEspecial("Mariana", "2002", saldo=200, limite=300)

    print("--- Tentativa de saque de R$ 350 na conta comum ---")
    conta_comum.saque(350)  # Deve falhar

    print("\n--- Tentativa de saque de R$ 350 na conta especial ---")
    conta_especial.saque(350)  # Deve ser autorizado (usa 200 de saldo + 150 do limite)
    print(f"Novo saldo da conta especial: R$ {conta_especial.saldo:.2f}")
