"""
Exercício 9.33 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que leia um diretório e gere uma página HTML contendo
uma galeria com links e miniaturas para todas as imagens encontradas
(extensões .jpg, .jpeg, .png, .gif, .svg).
"""

import os
import sys

EXTENSOES_IMAGEM = {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"}


def gerar_galeria_html(diretorio, arquivo_saida_html):
    if not os.path.exists(diretorio) or not os.path.isdir(diretorio):
        print(f"Erro: Diretório '{diretorio}' inválido ou não encontrado.")
        return

    imagens = []
    for item in os.listdir(diretorio):
        ext = os.path.splitext(item)[1].lower()
        if ext in EXTENSOES_IMAGEM:
            imagens.append(item)

    html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Galeria de Imagens - {diretorio}</title>
    <style>
        body {{ font-family: sans-serif; margin: 20px; background: #fafafa; }}
        .grid {{ display: flex; flex-wrap: wrap; gap: 15px; }}
        .item {{ border: 1px solid #ccc; background: white; padding: 10px; border-radius: 4px; text-align: center; }}
        img {{ max-width: 200px; max-height: 150px; display: block; margin: 0 auto 10px; }}
    </style>
</head>
<body>
    <h2>Galeria de Imagens de '{diretorio}'</h2>
    <p>Total de imagens encontradas: {len(imagens)}</p>
    <div class="grid">
"""
    for img in sorted(imagens):
        caminho_rel = os.path.join(diretorio, img).replace("\\", "/")
        html += f"""        <div class="item">
            <a href="{caminho_rel}" target="_blank">
                <img src="{caminho_rel}" alt="{img}">
                <span>{img}</span>
            </a>
        </div>
"""

    html += """    </div>
</body>
</html>"""

    with open(arquivo_saida_html, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Galeria HTML gerada em '{arquivo_saida_html}' com {len(imagens)} imagens.")


if __name__ == "__main__":
    pasta_teste = "temp_galeria"
    os.makedirs(pasta_teste, exist_ok=True)

    # Criação de arquivos de imagem fictícios para o teste
    for nome in ["foto1.png", "foto2.jpg", "documento.txt"]:
        with open(os.path.join(pasta_teste, nome), "w", encoding="utf-8") as f:
            f.write("mock")

    html_out = "temp_galeria.html"
    gerar_galeria_html(pasta_teste, html_out)

    # Limpeza
    for item in os.listdir(pasta_teste):
        os.remove(os.path.join(pasta_teste, item))
    os.rmdir(pasta_teste)
    if os.path.exists(html_out):
        os.remove(html_out)
