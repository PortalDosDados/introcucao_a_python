"""
Exercício 6.2 Faça um programa que leia duas listas e que gere uma terceira com
os elementos das duas primeiras.
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

terceira = primeira[:]
terceira.extend(segunda)

print(f"\nPrimeira lista: {primeira}")
print(f"Segunda lista: {segunda}")
print(f"Terceira lista (junção): {terceira}")
