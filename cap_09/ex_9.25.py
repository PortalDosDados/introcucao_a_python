"""
Exercício 9.25 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Adicione à agenda a opção de importar contatos a partir de um arquivo CSV,
salvando os novos registros no arquivo texto de dados da agenda.
"""

import os
import csv


def importar_de_csv(arquivo_origem_csv, arquivo_destino_txt):
    if not os.path.exists(arquivo_origem_csv):
        print(f"Erro: Arquivo CSV '{arquivo_origem_csv}' não encontrado.")
        return 0

    novos_contatos = []
    with open(arquivo_origem_csv, "r", encoding="utf-8") as f_csv:
        leitor = csv.reader(f_csv, delimiter=";")
        linhas = list(leitor)
        if not linhas:
            return 0

        # Identifica se a primeira linha é cabeçalho
        primeira_linha = linhas[0]
        inicio = 1 if "nome" in primeira_linha[0].lower() else 0

        for row in linhas[inicio:]:
            if len(row) >= 2 and row[0].strip():
                novos_contatos.append([row[0].strip(), row[1].strip()])

    with open(arquivo_destino_txt, "a", encoding="utf-8") as f_txt:
        for nome, tel in novos_contatos:
            f_txt.write(f"{nome}#{tel}\n")

    print(f"Importados {len(novos_contatos)} contatos para '{arquivo_destino_txt}'.")
    return len(novos_contatos)


if __name__ == "__main__":
    arq_csv = "temp_origem_ex9_25.csv"
    arq_txt = "temp_agenda_ex9_25.txt"

    with open(arq_csv, "w", encoding="utf-8", newline="") as f:
        f.write("Nome;Telefone\n")
        f.write("Eduardo Gomes;91234-5678\n")
        f.write("Fernanda Rocha;92345-6789\n")

    importar_de_csv(arq_csv, arq_txt)

    print(f"\n--- Conteúdo do arquivo texto após importação ({arq_txt}) ---")
    with open(arq_txt, "r", encoding="utf-8") as f:
        print(f.read(), end="")

    for f in [arq_csv, arq_txt]:
        if os.path.exists(f):
            os.remove(f)
