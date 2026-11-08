"""
Exercício 5.15 Escreva um programa para controlar uma pequena máquina registradora.
Você deve solicitar ao usuário que digite o código do produto e a quantidade
comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto:
Código 1: R$ 0,50
Código 2: R$ 1,00
Código 3: R$ 4,00
Código 5: R$ 7,00
Código 9: R$ 8,00
Qualquer outro código deve gerar a mensagem de erro "Código inválido".
O programa deve parar quando o código 0 for digitado.
"""

total = 0.0

while True:
    codigo = int(input("Código do produto (0 para sair): "))
    if codigo == 0:
        break

    preco = 0.0
    if codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print("Código inválido.")
        continue

    quantidade = int(input("Quantidade: "))
    total = total + (preco * quantidade)

print(f"Total das compras: R$ {total:.2f}")
