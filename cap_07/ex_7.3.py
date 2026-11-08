"""
Exercício 7.3 Escreva um programa que leia duas strings e gere uma terceira apenas
com os caracteres que aparecem em uma delas (ou seja, caracteres não comuns).
1ª string: CTA
2ª string: ABC
Resultado: T B (ou TB)
"""

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

resultado = []

for c in primeira:
    if c not in segunda and c not in resultado:
        resultado.append(c)

for c in segunda:
    if c not in primeira and c not in resultado:
        resultado.append(c)

terceira = "".join(resultado)
print(f"Caracteres não comuns: {terceira}")
