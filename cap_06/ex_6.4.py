"""
Exercício 6.4 O que acontece se a fila estiver vazia e tentarmos atender um
cliente (no Programa 6.7)?

Resposta:
No Programa 6.7, o atendimento é realizado através do método `fila.pop(0)`.
Se a lista `fila` estiver vazia (tamanho 0), a chamada a `fila.pop(0)` levantará
uma exceção do tipo `IndexError: pop from empty list`, interrompendo abruptamente
a execução do programa.

A solução consiste em verificar se a lista possui elementos antes de tentar remover:
`if len(fila) > 0:` atender o cliente; `else:` exibir mensagem informando que a fila
está vazia.
"""

ultimo = 0
fila = []

while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("A para realizar o atendimento ou S para sair.")
    operacao = input("Operação (F, A ou S): ").upper()

    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido.")
        else:
            print("Fila vazia! Nenhum cliente para atender.")
    elif operacao == "F":
        ultimo = ultimo + 1
        fila.append(ultimo)
    elif operacao == "S":
        print("Encerrando o programa.")
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S.")
