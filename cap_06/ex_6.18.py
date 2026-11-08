"""
Exercício 6.18 Escreva um programa que gere um dicionário onde cada chave seja
um caractere e seu valor seja o número de ocorrências desse caractere na string lida.
Exemplo: frase = "o rato roeu a roupa do rei de roma"
"""

frase = input("Digite uma frase ou palavra: ")
contagem = {}

for caractere in frase:
    if caractere in contagem:
        contagem[caractere] = contagem[caractere] + 1
    else:
        contagem[caractere] = 1

print("\nOcorrências de caracteres:")
for chave, valor in contagem.items():
    print(f"'{chave}': {valor}")
