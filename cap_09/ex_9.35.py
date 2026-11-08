"""
Exercício 9.35 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que gere uma página HTML com a lista de todos os arquivos e
subdiretórios de uma pasta informada, exibindo nome, tipo (arquivo ou diretório),
tamanho em bytes e data da última modificação.
"""

import os
import sys
import time


def gerar_relatorio_diretorio_html(diretorio, arquivo_saida_html):
    if not os.path.exists(diretorio) or not os.path.isdir(diretorio):
        print(f"Erro: '{diretorio}' não é um diretório válido.")
        return

    itens = os.listdir(diretorio)

    html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Inventário de Arquivos - {diretorio}</title>
    <style>
        body {{ font-family: sans-serif; margin: 30px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #34495e; color: white; }}
        tr:nth-child(even) {{ background-color: #f9f9f9; }}
    </style>
</head>
<body>
    <h2>Inventário do Diretório: {os.path.abspath(diretorio)}</h2>
    <table>
        <thead>
            <tr>
                <th>Nome</th>
                <th>Tipo</th>
                <th>Tamanho (bytes)</th>
                <th>Última Modificação</th>
            </tr>
        </thead>
        <tbody>
"""
    for item in sorted(itens):
        caminho_completo = os.path.join(diretorio, item)
        tipo = "Diretório" if os.path.isdir(caminho_completo) else "Arquivo"
        tamanho = (
            "-"
            if os.path.isdir(caminho_completo)
            else os.path.getsize(caminho_completo)
        )
        modificacao = time.strftime(
            "%d/%m/%Y %H:%M:%S", time.localtime(os.path.getmtime(caminho_completo))
        )

        html += f"""            <tr>
                <td>{item}</td>
                <td>{tipo}</td>
                <td>{tamanho}</td>
                <td>{modificacao}</td>
            </tr>\n"""

    html += """        </tbody>
    </table>
</body>
</html>"""

    with open(arquivo_saida_html, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Inventário salvo com sucesso em '{arquivo_saida_html}'.")


if __name__ == "__main__":
    caminho_alvo = sys.argv[1] if len(sys.argv) > 1 else "."
    saida = "temp_inventario.html"

    gerar_relatorio_diretorio_html(caminho_alvo, saida)

    if os.path.exists(saida):
        os.remove(saida)
