"""
Exercício 6.5 Altere o Programa 6.7 de forma a poder trabalhar com vários
comandos digitados de uma só vez. Atualmente, apenas um comando pode ser inserido
por vez. Um exemplo de uso desse novo programa seria a digitação de "FFAA" para
inserir dois clientes na fila e realizar dois atendimentos.
"""

ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente, A para atender ou S para sair.")
    operacoes = input("Operações a executar: ").upper()

    sair = False
    for op in operacoes:
        if op == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif op == "F":
            ultimo = ultimo + 1
            fila.append(ultimo)
            print(f"Cliente {ultimo} entrou na fila.")
        elif op == "S":
            sair = True
            break
        else:
            print(f"Operação inválida: {op}")

    if sair:
        print("Encerrando o programa.")
        break
