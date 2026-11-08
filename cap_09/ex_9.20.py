"""
Exercício 9.20 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Altere a agenda telefônica para permitir a alteração dos dados (edição de nome
ou telefone) de um contato existente no arquivo.
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


def alterar_contato(arquivo, nome_antigo, novo_nome=None, novo_telefone=None):
    agenda = carregar_agenda(arquivo)
    alterado = False

    for contato in agenda:
        if contato[0].lower() == nome_antigo.lower():
            if novo_nome:
                contato[0] = novo_nome
            if novo_telefone:
                contato[1] = novo_telefone
            alterado = True
            break

    if alterado:
        salvar_agenda(arquivo, agenda)
        print(f"Contato '{nome_antigo}' atualizado com sucesso.")
    else:
        print(f"Contato '{nome_antigo}' não encontrado.")

    return alterado


if __name__ == "__main__":
    arq_demo = "temp_agenda_ex9_20.txt"
    contatos_iniciais = [["Alice", "1111"], ["Carlos", "3333"]]
    salvar_agenda(arq_demo, contatos_iniciais)

    print("Antes da edição:")
    print(carregar_agenda(arq_demo))

    alterar_contato(
        arq_demo, "Carlos", novo_nome="Carlos Eduardo", novo_telefone="9999-3333"
    )

    print("\nDepois da edição:")
    print(carregar_agenda(arq_demo))

    if os.path.exists(arq_demo):
        os.remove(arq_demo)
