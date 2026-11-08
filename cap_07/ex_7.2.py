"""
Exercício 7.2 Escreva um programa que leia duas strings e gere uma terceira com
os caracteres comuns às duas strings.
1ª string: AAACTBF
2ª string: CBT
Resultado: CBT
A ordem dos caracteres da terceira string não é importante, mas deve conter
apenas os caracteres que aparecem em ambas sem duplicações.
"""

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

comuns = []
for caractere in primeira:
    if caractere in segunda and caractere not in comuns:
        comuns.append(caractere)

resultado = "".join(comuns)
print(f"Caracteres comuns: {resultado}")
