"""
Exercício 6.3 Faça um programa que percorra duas listas e gere uma terceira sem
elementos repetidos.
"""

primeira = []
segunda = []

print("Preencha a primeira lista (digite 0 para encerrar):")
while True:
    e = int(input("Valor: "))
    if e == 0:
        break
    primeira.append(e)

print("\nPreencha a segunda lista (digite 0 para encerrar):")
while True:
    e = int(input("Valor: "))
    if e == 0:
        break
    segunda.append(e)

terceira = []

# Adiciona elementos da primeira lista que ainda não estão na terceira
for e in primeira:
    if e not in terceira:
        terceira.append(e)

# Adiciona elementos da segunda lista que ainda não estão na terceira
for e in segunda:
    if e not in terceira:
        terceira.append(e)

print(f"\nPrimeira lista: {primeira}")
print(f"Segunda lista: {segunda}")
print(f"Terceira lista sem repetições: {terceira}")
