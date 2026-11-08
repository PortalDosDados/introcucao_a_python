"""
Exercício 7.4 Escreva um programa que leia uma string e imprima quantas vezes
cada caractere aparece nessa string.
Exemplo: string = "TBT"
Resultado:
T: 2x
B: 1x
"""

texto = input("Digite uma string: ")
contagem = {}

for caractere in texto:
    contagem[caractere] = contagem.get(caractere, 0) + 1

print("\nOcorrências:")
for caractere, total in contagem.items():
    print(f"{caractere}: {total}x")
