"""
Exercício 6.14 O que acontece se a lista já estiver vazia ou com apenas um
elemento no programa de ordenação por bolhas (Programa 6.20)?

Resposta:
No Programa 6.20, a condição do laço principal é `while fim > 1:`, onde `fim = len(L)`.
- Se a lista estiver vazia (`len(L) == 0`): `fim` vale 0. A condição `0 > 1` é falsa logo
  na primeira avaliação. O laço nunca é executado e a lista vazia é preservada sem erros.
- Se a lista possuir um único elemento (`len(L) == 1`): `fim` vale 1. A condição `1 > 1`
  também é falsa. O laço não é executado e a lista com um elemento permanece inalterada.

Portanto, em ambos os casos o programa funciona perfeitamente sem gerar exceções.
"""

# Demonstração prática com lista vazia e com 1 elemento
listas_teste = [[], [42]]

for l in listas_teste:
    print(f"\nOrdenando lista: {l}")
    fim = len(l)
    while fim > 1:
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
    print(f"Resultado final: {l}")
