"""
Modulo Bonus: Suite de Testes Automatizados para ContaBancaria.

Desenvolvido com o padrao AAA (Arrange, Act, Assert) e compativel tanto com o
runner nativo do Python (unittest) quanto com o Pytest.
"""

import os
import sys
import unittest

# Assegura que o modulo conta_bancaria seja localizado independentemente do diretorio de execucao
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from conta_bancaria import ContaBancaria


class TestContaBancaria(unittest.TestCase):
    """Testes unitarios para a classe ContaBancaria."""

    # -------------------------------------------------------------------------
    # Ciclo 1: Criacao da conta e saldo inicial
    # -------------------------------------------------------------------------
    def test_deve_criar_conta_com_saldo_e_limite_padrao(self) -> None:
        # Arrange & Act
        conta = ContaBancaria(titular="Dione")

        # Assert
        self.assertEqual(conta.titular, "Dione")
        self.assertEqual(conta.saldo, 0.0)
        self.assertEqual(conta.limite, 0.0)
        self.assertEqual(conta.saldo_disponivel, 0.0)

    def test_deve_criar_conta_com_saldo_inicial_e_limite_definidos(self) -> None:
        # Arrange & Act
        conta = ContaBancaria(titular="Maria", saldo_inicial=200.0, limite=500.0)

        # Assert
        self.assertEqual(conta.saldo, 200.0)
        self.assertEqual(conta.limite, 500.0)
        self.assertEqual(conta.saldo_disponivel, 700.0)

    def test_deve_rejeitar_saldo_inicial_ou_limite_negativos(self) -> None:
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            ContaBancaria(titular="Invalido", saldo_inicial=-50.0)

        with self.assertRaises(ValueError):
            ContaBancaria(titular="Invalido", limite=-100.0)

    # -------------------------------------------------------------------------
    # Ciclo 2 e 3: Depositos
    # -------------------------------------------------------------------------
    def test_deve_creditar_valor_positivo_ao_depositar(self) -> None:
        # 1. Arrange (Preparar)
        conta = ContaBancaria(titular="Carlos", saldo_inicial=100.0)

        # 2. Act (Agir)
        conta.depositar(150.0)

        # 3. Assert (Verificar)
        self.assertEqual(conta.saldo, 250.0)

    def test_deve_rejeitar_deposito_com_valor_zero_ou_negativo(self) -> None:
        # 1. Arrange
        conta = ContaBancaria(titular="Carlos", saldo_inicial=50.0)

        # 2. Act & 3. Assert
        with self.assertRaises(ValueError):
            conta.depositar(0.0)

        with self.assertRaises(ValueError):
            conta.depositar(-30.0)

        # Garante que o saldo nao foi alterado
        self.assertEqual(conta.saldo, 50.0)

    # -------------------------------------------------------------------------
    # Ciclo 4: Saque com saldo
    # -------------------------------------------------------------------------
    def test_deve_sacar_quando_houver_saldo_suficiente(self) -> None:
        # 1. Arrange
        conta = ContaBancaria(titular="Ana", saldo_inicial=300.0)

        # 2. Act
        conta.sacar(100.0)

        # 3. Assert
        self.assertEqual(conta.saldo, 200.0)

    # -------------------------------------------------------------------------
    # Ciclo 5: Saque utilizando limite especial (saldo fica negativo)
    # -------------------------------------------------------------------------
    def test_deve_permitir_saque_usando_limite_especial(self) -> None:
        # 1. Arrange (saldo de 100 + limite de 200 = 300 disponivel)
        conta = ContaBancaria(titular="Lucas", saldo_inicial=100.0, limite=200.0)

        # 2. Act (saque de 250 ultrapassa o saldo e entra no cheque especial)
        conta.sacar(250.0)

        # 3. Assert
        self.assertEqual(conta.saldo, -150.0)
        self.assertEqual(conta.saldo_disponivel, 50.0)

    # -------------------------------------------------------------------------
    # Ciclo 6: Rejeicao de saque quando excede saldo + limite
    # -------------------------------------------------------------------------
    def test_deve_rejeitar_saque_quando_ultrapassar_saldo_e_limite(self) -> None:
        # 1. Arrange (saldo 50 + limite 100 = 150 disponivel)
        conta = ContaBancaria(titular="Pedro", saldo_inicial=50.0, limite=100.0)

        # 2. Act & 3. Assert
        with self.assertRaises(ValueError):
            conta.sacar(151.0)

        # Saldo permanece intacto
        self.assertEqual(conta.saldo, 50.0)

    def test_deve_rejeitar_saque_com_valor_zero_ou_negativo(self) -> None:
        # 1. Arrange
        conta = ContaBancaria(titular="Julia", saldo_inicial=100.0)

        # 2. Act & 3. Assert
        with self.assertRaises(ValueError):
            conta.sacar(0.0)

        with self.assertRaises(ValueError):
            conta.sacar(-20.0)

        self.assertEqual(conta.saldo, 100.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
