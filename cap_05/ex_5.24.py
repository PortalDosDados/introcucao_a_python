"""
Exercício 5.24 Modifique o programa anterior de forma a ler um número n.
Imprima os n primeiros números primos.
"""

n = int(input("Quantos números primos você deseja imprimir? "))

if n <= 0:
    print("Quantidade inválida. Digite um número positivo.")
else:
    encontrados = 0
    candidato = 2

    while encontrados < n:
        if candidato == 2:
            print(candidato)
            encontrados = encontrados + 1
        elif candidato % 2 != 0:
            divisor = 3
            eh_primo = True
            while divisor * divisor <= candidato:
                if candidato % divisor == 0:
                    eh_primo = False
                    break
                divisor = divisor + 2

            if eh_primo:
                print(candidato)
                encontrados = encontrados + 1

        candidato = candidato + 1
