"""
Exercício 6.19 Escreva um programa que compare duas listas. Utilizando operações
com conjuntos (set), gere:
- Os valores comuns às duas listas (interseção)
- Os valores que só existem na primeira (diferença A - B)
- Os valores que só existem na segunda (diferença B - A)
- Uma lista com elementos não repetidos das duas listas (união)
- Os elementos que aparecem apenas em uma das duas listas (diferença simétrica)
"""

lista_a = [1, 2, 3, 4, 5, 6]
lista_b = [4, 5, 6, 7, 8, 9]

conjunto_a = set(lista_a)
conjunto_b = set(lista_b)

comuns = conjunto_a & conjunto_b
so_na_primeira = conjunto_a - conjunto_b
so_na_segunda = conjunto_b - conjunto_a
uniao = conjunto_a | conjunto_b
apenas_em_uma = conjunto_a ^ conjunto_b

print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Comuns às duas listas: {comuns}")
print(f"Apenas na primeira lista: {so_na_primeira}")
print(f"Apenas na segunda lista: {so_na_segunda}")
print(f"Elementos não repetidos das duas listas (união): {uniao}")
print(f"Elementos não repetidos que aparecem em apenas uma lista: {apenas_em_uma}")
