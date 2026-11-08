"""
Exercício 9.24 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Adicione à agenda telefônica uma função para exportar os contatos cadastrados
para o formato CSV (valores separados por vírgula), incluindo linha de cabeçalho.
"""

import os
import csv


def exportar_para_csv(arquivo_origem_txt, arquivo_destino_csv):
    if not os.path.exists(arquivo_origem_txt):
        print(f"Erro: Arquivo '{arquivo_origem_txt}' não encontrado.")
        return

    contatos = []
    with open(arquivo_origem_txt, "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split("#")
            if len(partes) >= 2:
                contatos.append([partes[0], partes[1]])

    with open(arquivo_destino_csv, "w", encoding="utf-8", newline="") as f_csv:
        escritor = csv.writer(f_csv, delimiter=";")
        escritor.writerow(["Nome", "Telefone"])
        escritor.writerows(contatos)

    print(
        f"Exportação para '{arquivo_destino_csv}' concluída ({len(contatos)} contatos)."
    )


if __name__ == "__main__":
    arq_txt = "temp_agenda_ex9_24.txt"
    arq_csv = "temp_agenda_ex9_24.csv"

    with open(arq_txt, "w", encoding="utf-8") as f:
        f.write("Ana Paula#98888-0001\n")
        f.write("Carlos Alberto#98888-0002\n")

    exportar_para_csv(arq_txt, arq_csv)

    print(f"\n--- Conteúdo do CSV ({arq_csv}) ---")
    with open(arq_csv, "r", encoding="utf-8") as f:
        print(f.read(), end="")

    for f in [arq_txt, arq_csv]:
        if os.path.exists(f):
            os.remove(f)
