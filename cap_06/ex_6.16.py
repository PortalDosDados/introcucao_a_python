"""
Exercício 6.16 Modifique o Programa 6.20 para ordenar a lista em ordem decrescente.
"""

l = [1, 2, 3, 4, 5]
fim = len(l)

while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        # Para ordem decrescente, trocamos quando o elemento atual for menor que o próximo
        if l[x] < l[x + 1]:
            trocou = True
            temp = l[x]
            l[x] = l[x + 1]
            l[x + 1] = temp
        x = x + 1
    if not trocou:
        break
    fim = fim - 1

print(f"Lista ordenada em ordem decrescente: {l}")
