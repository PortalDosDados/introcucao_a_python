"""
Exercício 6.9 Modifique o Programa 6.9 de forma a pesquisar dois valores.
O programa deve imprimir também se o primeiro ou o segundo foi achado primeiro.
"""

l = [15, 7, 27, 39, 42, 10, 8]
p = int(input("Digite o primeiro valor a procurar: "))
v = int(input("Digite o segundo valor a procurar: "))

achou_p = -1
achou_v = -1
x = 0

while x < len(l):
    if l[x] == p and achou_p == -1:
        achou_p = x
    if l[x] == v and achou_v == -1:
        achou_v = x
    x = x + 1

if achou_p != -1:
    print(f"{p} foi encontrado na posição {achou_p}.")
else:
    print(f"{p} não foi encontrado.")

if achou_v != -1:
    print(f"{v} foi encontrado na posição {achou_v}.")
else:
    print(f"{v} não foi encontrado.")

if achou_p != -1 and achou_v != -1:
    if achou_p < achou_v:
        print(f"O primeiro valor ({p}) foi encontrado antes do segundo ({v}).")
    elif achou_v < achou_p:
        print(f"O segundo valor ({v}) foi encontrado antes do primeiro ({p}).")
    else:
        print("Os dois valores são idênticos e foram encontrados na mesma posição.")
