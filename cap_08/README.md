# Capítulo 8 ■ Funções

Funções são blocos de código nomeados e reutilizáveis criados para executar tarefas específicas. Elas permitem modularizar programas, evitar repetição de código, aumentar a legibilidade e facilitar a manutenção e os testes.

---

## 8.1 Definindo Funções (`def`)

Uma função é declarada usando a palavra-chave `def`, seguida pelo nome da função, parâmetros entre parênteses e dois pontos:

```python
def saudacao(nome):
    print(f"Olá, {nome}!")


saudacao("Maria")
```

---

## 8.2 Retorno de Valores (`return`)

Para devolver um resultado ao chamador, utilizamos `return`. Se uma função terminar sem executar `return`, ela retorna implicitamente `None`.

```python
def soma(a, b):
    return a + b


resultado = soma(10, 25)
print(resultado)  # 35
```

---

## 8.3 Escopo de Variáveis (Locais vs. Globais)

- **Variáveis Locais**: Criadas dentro do corpo da função, existem apenas durante a sua execução.
- **Variáveis Globais**: Declaradas fora de funções, acessíveis para leitura em qualquer ponto. Para alterá-las dentro de uma função, utiliza-se a palavra-chave `global`.

```python
total = 0  # Global


def acumula(valor):
    global total
    total += valor
```

---

## 8.4 Parâmetros Opcionais e Valores Padrão

Podemos definir valores padrão para parâmetros. Parâmetros com valores padrão devem vir após os parâmetros obrigatórios.

```python
def barra(tamanho=40, caractere="*"):
    print(caractere * tamanho)


barra()  # 40 asteriscos
barra(20, "-")  # 20 traços
```

---

## 8.5 Funções Recursivas

Uma função recursiva chama a si mesma para resolver instâncias menores do mesmo problema até alcançar um **caso base** (condição de parada).

```python
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)
```

---

## 8.6 Empacotamento e Desempacotamento (`*args` e `**kwargs`)

- `*args`: Empacota múltiplos argumentos posicionais em uma **tupla**.
- `**kwargs`: Empacota múltiplos argumentos nomeados em um **dicionário**.

```python
def soma_multiplos(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total
```

---

## 8.7 Funções Lambda (Expressões Anônimas)

Expressões `lambda` criam pequenas funções anônimas em uma única linha:

```python
dobro = lambda x: x * 2
print(dobro(5))  # 10
```

---

## 8.8 Módulos e Funções Integradas (`random`)

O capítulo aborda a utilização de módulos da biblioteca padrão, como `random`, para sorteios e escolhas aleatórias:

```python
import random

itens = ["pedra", "papel", "tesoura"]
sorteado = random.choice(itens)
```
