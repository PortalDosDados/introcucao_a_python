"""
Exercício 6.10 Modifique o programa anterior para pesquisar dois valores em uma
lista, informando também a posição onde cada um foi encontrado.
"""

l = [15, 7, 27, 39, 52, 10, 8]
p = int(input("Digite o primeiro valor a pesquisar: "))
v = int(input("Digite o segundo valor a pesquisar: "))

posicao_p = -1
posicao_v = -1
x = 0

while x < len(l):
    if l[x] == p and posicao_p == -1:
        posicao_p = x
    if l[x] == v and posicao_v == -1:
        posicao_v = x
    x = x + 1

if posicao_p != -1:
    print(f"Primeiro valor ({p}) encontrado na posição {posicao_p}.")
else:
    print(f"Primeiro valor ({p}) não encontrado.")

if posicao_v != -1:
    print(f"Segundo valor ({v}) encontrado na posição {posicao_v}.")
else:
    print(f"Segundo valor ({v}) não encontrado.")

if posicao_p != -1 and posicao_v != -1:
    if posicao_p < posicao_v:
        print(
            f"O valor {p} (posição {posicao_p}) foi encontrado antes de {v} (posição {posicao_v})."
        )
    elif posicao_v < posicao_p:
        print(
            f"O valor {v} (posição {posicao_v}) foi encontrado antes de {p} (posição {posicao_p})."
        )
    else:
        print(f"Os dois valores são iguais e estão na mesma posição: {posicao_p}.")
