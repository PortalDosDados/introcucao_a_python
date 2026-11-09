"""
Modulo Bonus: Implementacao da ContaBancaria construida via TDD.

Este modulo contem a classe ContaBancaria com regras de negocio para deposito,
saque e gestao de limite especial, desenvolvida seguindo o ciclo
Red-Green-Refactor.
"""


class ContaBancaria:
    """Representa uma conta bancaria com saldo e limite de cheque especial."""

    def __init__(
        self, titular: str, saldo_inicial: float = 0.0, limite: float = 0.0
    ) -> None:
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial nao pode ser negativo.")
        if limite < 0:
            raise ValueError("O limite nao pode ser negativo.")

        self.titular: str = titular
        self.saldo: float = float(saldo_inicial)
        self.limite: float = float(limite)

    @property
    def saldo_disponivel(self) -> float:
        """Retorna o saldo total disponivel somando o saldo e o limite."""
        return self.saldo + self.limite

    def depositar(self, valor: float) -> None:
        """Credita um valor positivo no saldo da conta."""
        if valor <= 0:
            raise ValueError("O valor do deposito deve ser maior que zero.")
        self.saldo += valor

    def sacar(self, valor: float) -> None:
        """Debita um valor caso haja saldo e limite disponiveis."""
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")

        if valor > self.saldo_disponivel:
            raise ValueError("Saldo e limite insuficientes para realizar o saque.")

        self.saldo -= valor
