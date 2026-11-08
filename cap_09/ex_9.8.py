"""
Exercício 9.8 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Modifique o programa do exercício anterior para também considerar a largura
máxima da linha (largura da página em caracteres). Se uma linha for mais longa
que a largura permitida, quebre-a em várias linhas respeitando o limite.
"""

import sys
import os


def quebrar_linha(linha, largura_maxima):
    linhas_quebradas = []
    linha_limpa = linha.rstrip("\r\n")

    if not linha_limpa:
        return ["\n"]

    while len(linha_limpa) > largura_maxima:
        linhas_quebradas.append(linha_limpa[:largura_maxima] + "\n")
        linha_limpa = linha_limpa[largura_maxima:]

    if linha_limpa:
        linhas_quebradas.append(linha_limpa + "\n")

    return linhas_quebradas


def paginar_com_largura(
    arquivo_entrada, arquivo_saida, linhas_por_pagina=60, largura_maxima=76
):
    if not os.path.exists(arquivo_entrada):
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")
        return

    num_pagina = 1
    linhas_na_pagina = 0

    with (
        open(arquivo_entrada, "r", encoding="utf-8") as entrada,
        open(arquivo_saida, "w", encoding="utf-8") as saida,
    ):

        def cabecalho(p):
            sep = "=" * largura_maxima
            return f"{sep}\nArquivo: {arquivo_entrada} - Página: {p}\n{sep}\n"

        saida.write(cabecalho(num_pagina))

        for linha in entrada:
            partes = quebrar_linha(linha, largura_maxima)
            for parte in partes:
                if linhas_na_pagina >= linhas_por_pagina:
                    num_pagina += 1
                    saida.write(f"\n{cabecalho(num_pagina)}")
                    linhas_na_pagina = 0

                saida.write(parte)
                linhas_na_pagina += 1


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        paginar_com_largura(sys.argv[1], sys.argv[2])
    else:
        # Demonstração autônoma com limites reduzidos
        f_in, f_out = "temp_largura.txt", "temp_pag_largura.txt"
        with open(f_in, "w", encoding="utf-8") as f:
            f.write("Esta linha e bastante curta.\n")
            f.write(
                "Esta outra linha possui um texto extremamente longo que ultrapassa o limite de caracteres por linha.\n"
            )
            f.write("Fim do arquivo de teste.\n")

        paginar_com_largura(f_in, f_out, linhas_por_pagina=4, largura_maxima=30)

        print(f"--- Arquivo com quebra de largura gerado em '{f_out}' ---")
        with open(f_out, "r", encoding="utf-8") as res:
            print(res.read())

        for f in [f_in, f_out]:
            if os.path.exists(f):
                os.remove(f)
