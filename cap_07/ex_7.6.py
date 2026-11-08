"""
Exercício 7.6 Escreva um programa que leia três strings. Imprima o resultado da
substituição na primeira, dos caracteres da segunda pelos da terceira.
1ª: AATTCGAA
2ª: TG
3ª: AC
Resultado: AAAACCAA
"""

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string (caracteres a procurar): ")
terceira = input("Digite a terceira string (caracteres de substituição): ")

if len(segunda) != len(terceira):
    print("Erro: A segunda e a terceira strings devem ter exatamente o mesmo tamanho.")
else:
    resultado = []
    for c in primeira:
        posicao = segunda.find(c)
        if posicao != -1:
            resultado.append(terceira[posicao])
        else:
            resultado.append(c)

    final = "".join(resultado)
    print(f"Resultado da substituição: {final}")
