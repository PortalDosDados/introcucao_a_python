"""
Exercício 10.12 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Modifique a classe Conta para verificar se o valor solicitado no saque é maior
que o saldo disponível antes de debitar. Caso seja maior, impeça a operação,
exiba uma mensagem de alerta e retorne False, mantendo a integridade do saldo.
"""


class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.clientes = clientes if isinstance(clientes, list) else [clientes]
        self.numero = numero
        self.saldo = saldo
        self.operacoes = []

    def saque(self, valor):
        if valor <= 0:
            print("Erro: O valor de saque deve ser positivo.")
            return False

        if valor > self.saldo:
            print(
                f"Erro: Saque de R$ {valor:.2f} não permitido! "
                f"Saldo insuficiente (Saldo atual: R$ {self.saldo:.2f})."
            )
            return False

        self.saldo -= valor
        self.operacoes.append(["SAQUE", valor])
        print(f"Saque de R$ {valor:.2f} efetuado. Saldo restante: R$ {self.saldo:.2f}")
        return True

    def deposito(self, valor):
        if valor <= 0:
            print("Erro: O valor de depósito deve ser positivo.")
            return False

        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])
        return True


if __name__ == "__main__":
    conta = Conta(clientes="Felipe", numero="5544-3", saldo=150.0)

    print("Tentativa 1: Saque válido de R$ 50.00")
    conta.saque(50.0)

    print("\nTentativa 2: Saque inválido de R$ 200.00 (saldo de R$ 100.00)")
    conta.saque(200.0)

    print("\nTentativa 3: Saque com valor negativo")
    conta.saque(-10.0)
