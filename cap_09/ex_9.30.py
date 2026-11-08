"""
Exercício 9.30 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que leia um arquivo contendo uma lista de filmes (título, ano,
diretor e gênero) e gere uma página HTML formatando um catálogo dos filmes.
"""

import os


def gerar_catalogo_filmes_html(arquivo_origem_filmes, arquivo_saida_html):
    if not os.path.exists(arquivo_origem_filmes):
        print(f"Erro: Arquivo '{arquivo_origem_filmes}' não encontrado.")
        return

    filmes = []
    with open(arquivo_origem_filmes, "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) >= 4:
                filmes.append(
                    {
                        "titulo": partes[0].strip(),
                        "ano": partes[1].strip(),
                        "diretor": partes[2].strip(),
                        "genero": partes[3].strip(),
                    }
                )

    html = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Catálogo de Filmes</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; background-color: #f5f5f5; }
        .catalogo { display: flex; flex-wrap: wrap; gap: 20px; }
        .card { background: white; border: 1px solid #ddd; border-radius: 8px; padding: 15px; width: 250px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
        .titulo { font-size: 1.2em; font-weight: bold; color: #333; margin-bottom: 8px; }
        .info { color: #666; font-size: 0.9em; margin: 4px 0; }
    </style>
</head>
<body>
    <h1>Catálogo de Filmes</h1>
    <div class="catalogo">
"""
    for filme in filmes:
        html += f"""        <div class="card">
            <div class="titulo">{filme['titulo']}</div>
            <div class="info"><strong>Ano:</strong> {filme['ano']}</div>
            <div class="info"><strong>Diretor:</strong> {filme['diretor']}</div>
            <div class="info"><strong>Gênero:</strong> {filme['genero']}</div>
        </div>
"""

    html += """    </div>
</body>
</html>"""

    with open(arquivo_saida_html, "w", encoding="utf-8") as saida:
        saida.write(html)

    print(f"Catálogo HTML com {len(filmes)} filmes gerado em '{arquivo_saida_html}'.")


if __name__ == "__main__":
    arq_filmes = "temp_filmes.txt"
    arq_html = "temp_filmes.html"

    with open(arq_filmes, "w", encoding="utf-8") as f:
        f.write("O Poderoso Chefão;1972;Francis Ford Coppola;Drama / Crime\n")
        f.write("Interestelar;2014;Christopher Nolan;Ficção Científica\n")
        f.write("Matrix;1999;Lana e Lilly Wachowski;Ação / Sci-Fi\n")

    gerar_catalogo_filmes_html(arq_filmes, arq_html)

    for f in [arq_filmes, arq_html]:
        if os.path.exists(f):
            os.remove(f)
