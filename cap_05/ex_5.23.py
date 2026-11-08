"""
Exercício 5.23 Escreva um programa que leia um número e verifique se ele é ou não
um número primo. Para fazer essa verificação, calcule o resto da divisão do número
por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma
dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são
primos e que 2 é o único número primo que é par.
"""

n = int(input("Digite um número inteiro: "))

if n < 2:
    print(f"{n} não é um número primo.")
elif n == 2:
    print("2 é um número primo.")
elif n % 2 == 0:
    print(f"{n} não é um número primo (é par e maior que 2).")
else:
    divisor = 3
    eh_primo = True

    while divisor * divisor <= n:
        if n % divisor == 0:
            eh_primo = False
            break
        divisor = divisor + 2

    if eh_primo:
        print(f"{n} é um número primo.")
    else:
        print(f"{n} não é um número primo.")
