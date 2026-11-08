"""
Exercício 9.23 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Altere o programa de agenda para suportar múltiplos telefones com tipos
(ex.: celular, fixo, trabalho) e endereço de e-mail para cada contato.
"""

import os


def salvar_agenda_completa(arquivo, contatos):
    # Formato: nome#email#tipo1:num1,tipo2:num2
    with open(arquivo, "w", encoding="utf-8") as f:
        for c in contatos:
            telefones_str = ",".join([f"{tipo}:{num}" for tipo, num in c["telefones"]])
            f.write(f"{c['nome']}#{c['email']}#{telefones_str}\n")


def carregar_agenda_completa(arquivo):
    contatos = []
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split("#")
                if len(partes) >= 3:
                    nome, email, tels_brutos = partes[0], partes[1], partes[2]
                    telefones = []
                    if tels_brutos:
                        for item in tels_brutos.split(","):
                            if ":" in item:
                                tipo, num = item.split(":", 1)
                                telefones.append((tipo, num))
                    contatos.append(
                        {"nome": nome, "email": email, "telefones": telefones}
                    )
    return contatos


if __name__ == "__main__":
    arq_demo = "temp_agenda_ex9_23.txt"
    dados = [
        {
            "nome": "Carla Dias",
            "email": "carla@exemplo.com",
            "telefones": [("celular", "99111-2222"), ("trabalho", "3344-5566")],
        },
        {
            "nome": "Marcos Paulo",
            "email": "marcos@exemplo.com",
            "telefones": [("fixo", "3211-0099")],
        },
    ]

    salvar_agenda_completa(arq_demo, dados)
    carregados = carregar_agenda_completa(arq_demo)

    print("--- Agenda com Múltiplos Telefones e E-mail ---")
    for c in carregados:
        print(f"Nome: {c['nome']} | E-mail: {c['email']}")
        for tipo, num in c["telefones"]:
            print(f"  - {tipo.capitalize()}: {num}")

    if os.path.exists(arq_demo):
        os.remove(arq_demo)
