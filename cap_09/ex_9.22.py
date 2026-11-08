"""
Exercício 9.22 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Altere a agenda para ordenar a lista de contatos em ordem alfabética de nomes
antes de gravá-los no arquivo ou apresentá-los na tela.
"""

import os


def carregar_agenda(arquivo):
    agenda = []
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if "#" in linha:
                    nome, telefone = linha.split("#", 1)
                    agenda.append([nome, telefone])
    return agenda


def salvar_agenda_ordenada(arquivo, agenda):
    agenda_ordenada = sorted(agenda, key=lambda c: c[0].lower())
    with open(arquivo, "w", encoding="utf-8") as f:
        for nome, telefone in agenda_ordenada:
            f.write(f"{nome}#{telefone}\n")
    return agenda_ordenada


if __name__ == "__main__":
    arq_demo = "temp_agenda_ex9_22.txt"
    desordenados = [
        ["Zuleica Lima", "9111-0000"],
        ["Bruno Castro", "9222-0000"],
        ["Ana Clara", "9333-0000"],
    ]

    print("Contatos desordenados:")
    for n, t in desordenados:
        print(f"{n} - {t}")

    ordenados = salvar_agenda_ordenada(arq_demo, desordenados)

    print("\nContatos salvos e ordenados alfabeticamente:")
    for n, t in carregar_agenda(arq_demo):
        print(f"{n} - {t}")

    if os.path.exists(arq_demo):
        os.remove(arq_demo)
