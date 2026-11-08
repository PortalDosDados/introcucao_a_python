"""
Exercício 7.5 Escreva um programa que leia duas strings e gere uma terceira, na
qual os caracteres da segunda foram retirados da primeira.
1ª string: AATTGGAA
2ª string: TG
Resultado: AAAA
"""

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

resultado = []
for caractere in primeira:
    if caractere not in segunda:
        resultado.append(caractere)

terceira = "".join(resultado)
print(f"Resultado após remoção: {terceira}")
