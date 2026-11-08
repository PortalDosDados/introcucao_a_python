"""
Exercício 6.15 O que acontece se a lista já estiver ordenada no algoritmo de
ordenação por bolhas? Como otimizar?

Resposta:
No Programa 6.20 do livro, já existe a variável lógica `trocou`.
Quando a lista já se encontra perfeitamente ordenada:
1. O laço interno percorre todos os pares de elementos adjacentes realizando comparações.
2. Como nenhum elemento é maior que seu sucessor, a condição `L[x] > L[x + 1]` nunca é
   verdadeira, e a variável `trocou` permanece `False`.
3. Ao término da primeira passagem, a verificação `if not trocou: break` é acionada,
   interrompendo o algoritmo logo após a primeira rodada de comparações (complexidade O(n)).

Abaixo, demonstramos a contagem do número de passagens em uma lista já ordenada.
"""

l = [1, 2, 3, 4, 5, 6, 7]
print(f"Lista inicial (já ordenada): {l}")

fim = len(l)
passadas = 0

while fim > 1:
    passadas = passadas + 1
    trocou = False
    x = 0
    while x < (fim - 1):
        if l[x] > l[x + 1]:
            trocou = True
            temp = l[x]
            l[x] = l[x + 1]
            l[x + 1] = temp
        x = x + 1
    if not trocou:
        break
    fim = fim - 1

print(f"Número de passadas necessárias: {passadas}")
print(f"Lista final: {l}")
