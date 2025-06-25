'''

Exercício 4.8 

Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

'''


while True:

    try:

        n1 = float(input('Escolha 1 número: '))
        n2 = float(input('Escolha outro número: '))
        operação = input('Qual operação você quer realizar?').strip().lower()

        if operação == 'soma':
            resultado = n1+n2
            print(f'A soma do número {n1} e {n2} é {resultado}')

        elif operação == 'subtração':
            resultado = n1 - n2
            print(f'A subtração do número {n1} por {n2} é {resultado}')

        elif operação == 'divisão':
            resultado = n1 / n2
            print(f'A divisão do número {n1} por {n2} é {resultado}')

        elif operação == 'multiplicação':
            resultado = n1 * n2
            print(f'A multiplicação do número {n1} por {n2} é {resultado}')

        else:
            print('Operação invalida')

        break

    except Exception as erro:
        print ('Tente novamente')
