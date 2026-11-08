"""
Exercício 6.17 Altere o programa da Listagem 6.22 de forma a solicitar a
quantidade vendida de cada produto e atualizar o estoque.
"""

estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijao": [100, 1.50],
}

total = 0.0

print("Venda de produtos (digite 'fim' para encerrar):")
while True:
    produto = input("Nome do produto: ").lower()
    if produto == "fim":
        break

    if produto in estoque:
        quantidade = int(input("Quantidade comprada: "))
        if quantidade <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = preco * quantidade
            estoque[produto][0] = estoque[produto][0] - quantidade
            total = total + custo
            print(f"{produto}: {quantidade} x R$ {preco:.2f} = R$ {custo:.2f}")
            print(f"Estoque restante de {produto}: {estoque[produto][0]}")
        else:
            print(f"Quantidade indisponível! Estoque atual: {estoque[produto][0]}")
    else:
        print("Produto não encontrado no estoque.")

print(f"\nTotal da venda: R$ {total:.2f}")
print("\nEstoque final atualizado:")
for produto, dados in estoque.items():
    print(f"{produto:<10}: Quantidade = {dados[0]:4d} | Preço = R$ {dados[1]:.2f}")
