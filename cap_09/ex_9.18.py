"""
Exercício 9.18 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Modifique o programa de geração de HTML para incluir cores alternadas de fundo
nas linhas da tabela (efeito zebrado com atributos bgcolor ou classes CSS) e
apresentar o total de contatos listados no rodapé.
"""

import os


def gerar_agenda_zebrada_html(arquivo_saida, contatos):
    html = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Agenda Telefônica Estilizada</title>
    <style>
        table { border-collapse: collapse; width: 60%; font-family: sans-serif; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background-color: #2b5797; color: white; }
        .linha-par { background-color: #f2f2f2; }
        .linha-impar { background-color: #ffffff; }
        tfoot td { font-weight: bold; background-color: #e0e0e0; }
    </style>
</head>
<body>
    <h2>Agenda de Contatos</h2>
    <table>
        <thead>
            <tr>
                <th>Nome</th>
                <th>Telefone</th>
            </tr>
        </thead>
        <tbody>
"""
    for idx, (nome, telefone) in enumerate(contatos):
        classe_linha = "linha-par" if idx % 2 == 0 else "linha-impar"
        html += f'            <tr class="{classe_linha}"><td>{nome}</td><td>{telefone}</td></tr>\n'

    total = len(contatos)
    html += f"""        </tbody>
        <tfoot>
            <tr>
                <td colspan="2">Total de contatos cadastrados: {total}</td>
            </tr>
        </tfoot>
    </table>
</body>
</html>
"""
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    contatos_exemplo = [
        ("Alice Souza", "9811-1234"),
        ("Bruno Lima", "9822-2345"),
        ("Carla Mendes", "9833-3456"),
        ("Daniel Costa", "9844-4567"),
    ]
    saida = "temp_agenda_zebrada.html"
    gerar_agenda_zebrada_html(saida, contatos_exemplo)

    print(f"Página zebrada gerada em '{saida}'.")
    with open(saida, "r", encoding="utf-8") as f:
        print(f.read())

    if os.path.exists(saida):
        os.remove(saida)
