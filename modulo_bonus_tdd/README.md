# Módulo Bônus: Test-Driven Development (TDD) Passo a Passo

> *"Nunca escreva código de produção sem que haja antes um teste automatizado falhando."* — Kent Beck

---

## 🎯 1. O que é TDD?

**TDD** (*Test-Driven Development*, ou Desenvolvimento Guiado por Testes) é uma técnica de engenharia de software onde os **testes automatizados são escritos ANTES do código de produção**.

Em vez de programar primeiro e depois tentar descobrir como testar, você define os **requisitos, as entradas e as saídas esperadas** na forma de código executável.

---

## 🏭 2. A Ponte com a Indústria: TDD e o Ciclo PDCA

Se você já conhece métodos de qualidade industrial como o **PDCA (Plan-Do-Check-Act)** ou conceitos do Sistema Toyota de Produção (*Lean/Jidoka*), o TDD é uma transposição direta desses princípios para o software:

| Etapa Industrial (PDCA) | Etapa TDD | No Código de Teste (AAA) |
| :--- | :--- | :--- |
| **Plan (Planejar)** | **Especificação** | **Arrange (Preparar):** Definição das variáveis de entrada e condições iniciais da bancada. |
| **Do (Executar)** | **Processamento** | **Act (Agir):** Acionamento da máquina / chamada da função. |
| **Check (Checar / Inspecionar)** | **Controle de Qualidade** | **Assert (Verificar):** Medição com gabarito ou paquímetro se o resultado bateu com a tolerância esperada. |
| **Act (Ajustar / Melhorar)** | **Refatoração** | **Refactor:** Eliminação de desperdício, limpeza de código e otimização sem alterar o comportamento. |

> 💡 **Autonomação (*Jidoka*):** Assim como a linha de montagem para imediatamente se uma peça fora de especificação for detectada, no software a esteira de desenvolvimento para na hora se um teste falhar.

---

## 🔄 3. O Ciclo TDD: Red ➔ Green ➔ Refactor

O coração do TDD é um ciclo contínuo e rápido composto por três etapas:

```
  ┌────────────────────────────────────────────────────────┐
  │                                                        │
  ▼                                                        │
🔴 RED ──────────────► 🟢 GREEN ──────────────► 🔵 REFACTOR ─┘
(Escreva o teste       (Faça o teste           (Melhore o código
 que falha)             passar rápido)          mantendo verde)
```

1. **🔴 Red (Vermelho):**
   * Escreva um teste para o próximo pequeno comportamento que você deseja.
   * Execute o teste e **veja-o falhar** (garante que o teste realmente está medindo algo e não passa por acidente).

2. **🟢 Green (Verde):**
   * Escreva a implementação mais simples e direta possível para fazer o teste passar.
   * Não se preocupe com elegância neste segundo; o objetivo é sair do vermelho.

3. **🔵 Refactor (Refatorar):**
   * Com todos os testes verdes, limpe o código, elimine duplicações, melhore nomes de variáveis e otimize.
   * Execute os testes novamente: eles garantem que a refatoração não quebrou nada (*rede de proteção*).

---

## 📐 4. O Padrão AAA (Arrange, Act, Assert)

Todo método de teste unitário deve ser dividido mentalmente em três blocos bem delineados:

```python
def test_deve_creditar_valor_ao_depositar():
    # 1. Arrange (Preparar o cenário)
    conta = ContaBancaria(titular="Dione", saldo_inicial=100.0)

    # 2. Act (Executar a ação a ser testada)
    conta.depositar(50.0)

    # 3. Assert (Verificar o resultado esperado)
    assert conta.saldo == 150.0
```

---

## 🛠️ 5. Estudo de Caso Passo a Passo: `ContaBancaria`

Neste módulo, construímos uma classe `ContaBancaria` aplicando o ciclo TDD passo a passo:

### Ciclo 1: Criação da Conta e Saldo Inicial
* **🔴 Red:** Escrevemos `test_deve_criar_conta_com_saldo_inicial()`. Falhou com `NameError` (a classe nem existia).
* **🟢 Green:** Criamos a classe com `__init__` básico recebendo `titular` e `saldo_inicial`.
* **🔵 Refactor:** Adicionamos tipagem com Type Hints (`str`, `float`).

### Ciclo 2: Depósito Válido
* **🔴 Red:** Escrevemos `test_deve_depositar_valor_positivo()`. Falhou com `AttributeError` (método `depositar` inexistente).
* **🟢 Green:** Criamos o método `depositar(valor)` somando `self.saldo += valor`.
* **🔵 Refactor:** Verificação se o saldo continuava consistente.

### Ciclo 3: Validação de Depósito Negativo ou Zero
* **🔴 Red:** Escrevemos `test_deve_rejeitar_deposito_invalido()`. Falhou porque o código aceitou valor negativo.
* **🟢 Green:** Adicionamos validação com `ValueError("O valor do deposito deve ser maior que zero.")`.
* **🔵 Refactor:** Centralização das mensagens de erro.

### Ciclo 4: Saque com Saldo Suficiente
* **🔴 Red:** Escrevemos `test_deve_sacar_quando_houver_saldo()`.
* **🟢 Green:** Criamos método `sacar(valor)` subtraindo `self.saldo -= valor`.

### Ciclo 5: Saque com Limite Especial (Cheque Especial)
* **🔴 Red:** Escrevemos `test_deve_permitir_saque_usando_limite_especial()`. Falhou com saldo insuficiente.
* **🟢 Green:** Ajustamos o cálculo para permitir saque até `saldo + limite`.

### Ciclo 6: Rejeição de Saque sem Limite Suficiente
* **🔴 Red:** Escrevemos `test_deve_rejeitar_saque_superior_ao_limite()`.
* **🟢 Green:** Lançamento de `ValueError("Saldo e limite insuficientes para realizar o saque.")`.

---

## 🚀 6. Como Executar os Testes

O código foi planejado para rodar tanto **nativamente** (sem instalar nada) quanto via **`pytest`**:

### Opção A: Execução Nativa (Biblioteca Padrão do Python)
Não necessita de nenhuma instalação adicional:

```bash
# Executar a suíte de testes diretamente:
python modulo_bonus_tdd/test_conta_bancaria.py

# Ou usando o módulo nativo unittest:
python -m unittest modulo_bonus_tdd/test_conta_bancaria.py -v
```

### Opção B: Execução com Pytest (Opcional)
Se você instalar o `pytest` no seu ambiente (`pip install pytest`):

```bash
# Execução simples:
pytest modulo_bonus_tdd/

# Execução detalhada (verbose):
pytest modulo_bonus_tdd/ -v
```

---

## 🎓 Conclusão e Próximos Passos
Praticar TDD treina sua mente a pensar **no consumidor do seu código** antes de pensar nos detalhes internos da implementação. 

Tente aplicar esses 3 passos nos projetos integradores do curso (`PROJETOS_PRATICOS.md`)!
