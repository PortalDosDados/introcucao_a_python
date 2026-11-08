"""
Exercício 9.29 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que leia um arquivo de configuração (.ini simples) contendo
seções entre colchetes ([secao]) e pares de valores (chave = valor),
armazenando os dados em um dicionário estruturado e gerando uma página HTML.
"""

import os


def ler_arquivo_ini(caminho_ini):
    if not os.path.exists(caminho_ini):
        print(f"Erro: Arquivo '{caminho_ini}' não encontrado.")
        return {}

    config = {}
    secao_atual = "GERAL"

    with open(caminho_ini, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha or linha.startswith(";") or linha.startswith("#"):
                continue

            if linha.startswith("[") and linha.endswith("]"):
                secao_atual = linha[1:-1].strip()
                if secao_atual not in config:
                    config[secao_atual] = {}
            elif "=" in linha:
                chave, valor = linha.split("=", 1)
                chave = chave.strip()
                valor = valor.strip()
                if secao_atual not in config:
                    config[secao_atual] = {}
                config[secao_atual][chave] = valor

    return config


def exportar_config_html(config, arquivo_html):
    html = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Configurações do Sistema</title>
    <style>
        body { font-family: sans-serif; margin: 20px; }
        .secao { margin-bottom: 25px; border: 1px solid #ddd; padding: 10px; border-radius: 5px; }
        h3 { margin-top: 0; color: #1a5276; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #eee; padding: 6px; text-align: left; }
        th { background: #f8f9f9; }
    </style>
</head>
<body>
    <h2>Arquivo de Configuração</h2>
"""
    for secao, chaves in config.items():
        html += (
            f'    <div class="secao">\n        <h3>[{secao}]</h3>\n        <table>\n'
        )
        html += "            <tr><th>Chave</th><th>Valor</th></tr>\n"
        for k, v in chaves.items():
            html += f"            <tr><td><code>{k}</code></td><td>{v}</td></tr>\n"
        html += "        </table>\n    </div>\n"

    html += "</body>\n</html>"

    with open(arquivo_html, "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    ini_temp = "temp_config.ini"
    html_temp = "temp_config.html"

    with open(ini_temp, "w", encoding="utf-8") as f:
        f.write("[banco_dados]\n")
        f.write("host = localhost\n")
        f.write("porta = 5432\n")
        f.write("usuario = admin\n\n")
        f.write("[aplicacao]\n")
        f.write("debug = True\n")
        f.write("versao = 1.0.0\n")

    dados_config = ler_arquivo_ini(ini_temp)
    print("Dicionário de Configuração lido:")
    print(dados_config)

    exportar_config_html(dados_config, html_temp)
    print(f"\nHTML gerado em '{html_temp}'.")

    for f in [ini_temp, html_temp]:
        if os.path.exists(f):
            os.remove(f)
