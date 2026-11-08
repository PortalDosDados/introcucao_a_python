"""
Exercício 9.21 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Altere a agenda para permitir a pesquisa e busca de contatos por nome ou por
número de telefone, exibindo todos os resultados correspondentes.
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


def buscar_contato(arquivo, termo_busca):
    agenda = carregar_agenda(arquivo)
    termo = termo_busca.lower()
    encontrados = []

    for nome, telefone in agenda:
        if termo in nome.lower() or termo in telefone.lower():
            encontrados.append((nome, telefone))

    return encontrados


if __name__ == "__main__":
    arq_demo = "temp_agenda_ex9_21.txt"
    with open(arq_demo, "w", encoding="utf-8") as f:
        f.write("Alice Santos#98888-1111\n")
        f.write("Bernardo Silva#97777-2222\n")
        f.write("Alice Maria#96666-3333\n")

    print("Busca por 'Alice':")
    for n, t in buscar_contato(arq_demo, "Alice"):
        print(f"- {n}: {t}")

    print("\nBusca por telefone '7777':")
    for n, t in buscar_contato(arq_demo, "7777"):
        print(f"- {n}: {t}")

    if os.path.exists(arq_demo):
        os.remove(arq_demo)
