"""
Exercício 6.8 Modifique o Programa 6.9 de forma a não usar a variável `achou`
(flag) para indicar se o elemento foi encontrado.
"""

l = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
x = 0

while x < len(l):
    if l[x] == p:
        break
    x = x + 1

if x < len(l):
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não foi achado")
