"""
Exercício 9.6 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Modifique o programa de impressão de arquivos de forma que, caso uma linha
comece com o caractere ';' (ou qualquer caractere de comentário configurado),
ela não seja impressa (permitindo linhas de comentários no arquivo).
"""

import sys
import os


def imprimir_sem_comentarios(nome_arquivo, char_comentario=";"):
    if not os.path.exists(nome_arquivo):
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return

    with open(nome_arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            linha_limpa = linha.strip()
            if not linha_limpa.startswith(char_comentario):
                print(linha, end="")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        imprimir_sem_comentarios(sys.argv[1])
    else:
        # Demonstração autônoma
        arquivo_temp = "temp_comentarios.ini"
        with open(arquivo_temp, "w", encoding="utf-8") as f:
            f.write("; Este é um comentário que deve ser ignorado\n")
            f.write("servidor = localhost\n")
            f.write("; Outro comentário explicativo\n")
            f.write("porta = 8080\n")

        print("--- Conteúdo sem comentários ---")
        imprimir_sem_comentarios(arquivo_temp)

        if os.path.exists(arquivo_temp):
            os.remove(arquivo_temp)
