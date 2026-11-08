"""
Exercício 9.17 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Altere o Programa 9.5 de forma a gerar uma página HTML contendo uma tabela
formatada com borda (border='1') e cabeçalhos (tags <th>) para os campos
da agenda telefônica (Nome e Telefone).
"""

import os


def gerar_pagina_agenda_html(arquivo_saida, contatos):
    html = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Agenda Telefônica</title>
</head>
<body>
    <h1>Contatos da Agenda</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Nome</th>
                <th>Telefone</th>
            </tr>
        </thead>
        <tbody>
"""
    for nome, telefone in contatos:
        html += f"            <tr><td>{nome}</td><td>{telefone}</td></tr>\n"

    html += """        </tbody>
    </table>
</body>
</html>
"""
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    contatos_exemplo = [
        ("Maria Silva", "9999-1111"),
        ("João Santos", "8888-2222"),
        ("Ana Oliveira", "9777-3333"),
    ]
    saida = "temp_agenda.html"
    gerar_pagina_agenda_html(saida, contatos_exemplo)

    print(f"Página HTML gerada em '{saida}'.")
    with open(saida, "r", encoding="utf-8") as f:
        print(f.read())

    if os.path.exists(saida):
        os.remove(saida)
