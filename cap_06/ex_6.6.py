"""
Exercício 6.6 Modifique o programa anterior para trabalhar com duas filas: uma
fila normal e uma fila prioritária. Adicione comandos para entrada na fila normal
(F) e prioritária (P), atendimento na fila normal (A) e prioritária (B).
"""

ultimo_normal = 0
ultimo_prioritario = 0
fila_normal = []
fila_prioritaria = []

while True:
    print(f"\nFila normal ({len(fila_normal)}): {fila_normal}")
    print(f"Fila prioritária ({len(fila_prioritaria)}): {fila_prioritaria}")
    print("Comandos: F (chegada normal), P (chegada prioritária),")
    print("          A (atender normal), B (atender prioritária), S (sair)")
    operacoes = input("Digite a sequência de operações: ").upper()

    sair = False
    for op in operacoes:
        if op == "F":
            ultimo_normal = ultimo_normal + 1
            fila_normal.append(ultimo_normal)
            print(f"Cliente normal {ultimo_normal} adicionado.")
        elif op == "P":
            ultimo_prioritario = ultimo_prioritario + 1
            fila_prioritaria.append(ultimo_prioritario)
            print(f"Cliente prioritário {ultimo_prioritario} adicionado.")
        elif op == "A":
            if len(fila_normal) > 0:
                atendido = fila_normal.pop(0)
                print(f"Cliente normal {atendido} atendido.")
            else:
                print("Fila normal vazia!")
        elif op == "B":
            if len(fila_prioritaria) > 0:
                atendido = fila_prioritaria.pop(0)
                print(f"Cliente prioritário {atendido} atendido.")
            else:
                print("Fila prioritária vazia!")
        elif op == "S":
            sair = True
            break
        else:
            print(f"Operação inválida: {op}")

    if sair:
        print("Programa encerrado.")
        break
