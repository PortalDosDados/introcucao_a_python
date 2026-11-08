# Capítulo 5 ■ Repetições

As repetições representam uma das estruturas fundamentais da programação de computadores, permitindo que um bloco de instruções seja executado várias vezes até que uma condição seja satisfeita.

---

## 5.1 O comando `while`

O comando `while` executa um bloco de código repetidamente enquanto uma condição for verdadeira.

```python
while <condição>:
    bloco a ser repetido
```

- A condição é avaliada antes de cada repetição.
- Se a condição for falsa logo no início, o bloco não será executado nenhuma vez.
- Dentro do bloco, deve haver alguma instrução que modifique o valor testado na condição; caso contrário, ocorrerá um **laço infinito** (*infinite loop*).

---

## 5.2 Contadores

Um **contador** é uma variável utilizada para contar ocorrências de eventos ou passos em um laço.

```python
fim = int(input("Digite o último número a imprimir: "))
x = 1
while x <= fim:
    print(x)
    x = x + 1  # ou x += 1
```

---

## 5.3 Acumuladores

Um **acumulador** (ou somador) é uma variável que recebe a soma sucessiva de valores lidos ou calculados a cada iteração.
Diferente do contador (que normalmente incrementa um valor fixo como `+ 1`), o acumulador soma valores variáveis.

```python
n = 1
soma = 0
while n <= 10:
    x = int(input(f"Digite o {n}º número: "))
    soma = soma + x
    n = n + 1
print(f"Soma: {soma}")
```

---

## 5.4 Interrupção com `break`

A instrução `break` interrompe imediatamente a execução do laço `while`, transferindo o controle do fluxo para a primeira linha após o laço.

```python
soma = 0
while True:
    valor = int(input("Digite um número a somar ou 0 para sair: "))
    if valor == 0:
        break
    soma += valor
print(f"Total: {soma}")
```

---

## 5.5 Repetições aninhadas

Repetições aninhadas ocorrem quando um laço `while` é colocado dentro de outro laço `while`. São comuns em problemas bidimensionais (como tabuadas completas, matrizes ou combinações).

```python
tabuada = 1
while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print(f"{tabuada} x {numero} = {tabuada * numero}")
        numero += 1
    tabuada += 1
```
