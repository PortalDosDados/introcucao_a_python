"""
Exercício 5.14 Escreva um programa que leia números inteiros do teclado. O programa
deve ler os números até que o usuário digite 0 (zero). No final da execução,
exiba a quantidade de números digitados, assim como a soma e a média aritmética.
"""

quantidade = 0
soma = 0

while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    if numero == 0:
        break
    soma = soma + numero
    quantidade = quantidade + 1

if quantidade > 0:
    media = soma / quantidade
    print(f"Quantidade de números digitados: {quantidade}")
    print(f"Soma dos números digitados: {soma}")
    print(f"Média aritmética: {media:.2f}")
else:
    print("Nenhum número foi digitado.")
