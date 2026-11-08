"""
Exercício 9.19 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Altere o programa de agenda (Programa 9.6) para permitir a exclusão de um
contato registrado no arquivo de dados.
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


def salvar_agenda(arquivo, agenda):
    with open(arquivo, "w", encoding="utf-8") as f:
        for nome, telefone in agenda:
            f.write(f"{nome}#{telefone}\n")


def apagar_contato(arquivo, nome_para_apagar):
    agenda = carregar_agenda(arquivo)
    nova_agenda = [c for c in agenda if c[0].lower() != nome_para_apagar.lower()]

    removido = len(agenda) != len(nova_agenda)
    if removido:
        salvar_agenda(arquivo, nova_agenda)
        print(f"Contato '{nome_para_apagar}' removido com sucesso.")
    else:
        print(f"Contato '{nome_para_apagar}' não encontrado.")

    return removido


if __name__ == "__main__":
    arq_demo = "temp_agenda_ex9_19.txt"
    contatos_iniciais = [["Alice", "1111"], ["Bob", "2222"], ["Carlos", "3333"]]
    salvar_agenda(arq_demo, contatos_iniciais)

    print("Agenda antes da exclusão:")
    print(carregar_agenda(arq_demo))

    apagar_contato(arq_demo, "Bob")

    print("\nAgenda após a exclusão de 'Bob':")
    print(carregar_agenda(arq_demo))

    if os.path.exists(arq_demo):
        os.remove(arq_demo)
