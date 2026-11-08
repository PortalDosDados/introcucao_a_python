"""
Exercício 9.7 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie um programa que leia um arquivo-texto e gere um arquivo de saída paginado.
Cada página deve conter no máximo 60 linhas. No início de cada página deve ser
impresso o nome do arquivo e o número da página.
"""

import sys
import os


def paginar_arquivo(arquivo_entrada, arquivo_saida, linhas_por_pagina=60):
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
            return f"{'=' * 40}\nArquivo: {arquivo_entrada} - Página: {p}\n{'=' * 40}\n"

        saida.write(cabecalho(num_pagina))

        for linha in entrada:
            if linhas_na_pagina >= linhas_por_pagina:
                num_pagina += 1
                saida.write(f"\n{cabecalho(num_pagina)}")
                linhas_na_pagina = 0

            saida.write(linha)
            linhas_na_pagina += 1


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        paginar_arquivo(sys.argv[1], sys.argv[2])
    else:
        # Demonstração autônoma (usando 5 linhas por página para teste visual)
        f_in, f_out = "temp_longo.txt", "temp_paginado.txt"
        with open(f_in, "w", encoding="utf-8") as f:
            for i in range(1, 13):
                f.write(f"Registro de teste {i}\n")

        paginar_arquivo(f_in, f_out, linhas_por_pagina=5)

        print(f"--- Arquivo paginado gerado em '{f_out}' ---")
        with open(f_out, "r", encoding="utf-8") as res:
            print(res.read())

        for f in [f_in, f_out]:
            if os.path.exists(f):
                os.remove(f)
