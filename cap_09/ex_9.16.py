"""
Exercício 9.16 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Altere o jogo da forca para gravar e atualizar o recorde dos jogadores
(nome do jogador e pontuação de vitórias) em um arquivo texto ('recordes.txt').
"""

import os

ARQUIVO_RECORDES = "recordes.txt"


def carregar_recordes(caminho=ARQUIVO_RECORDES):
    recordes = {}
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if ":" in linha:
                    jogador, pontos = linha.split(":", 1)
                    try:
                        recordes[jogador.strip()] = int(pontos.strip())
                    except ValueError:
                        pass
    return recordes


def salvar_recorde(jogador, pontos, caminho=ARQUIVO_RECORDES):
    recordes = carregar_recordes(caminho)
    # Se o jogador já tem recorde anterior, atualiza apenas se a pontuação for maior
    if jogador in recordes:
        recordes[jogador] = max(recordes[jogador], pontos)
    else:
        recordes[jogador] = pontos

    with open(caminho, "w", encoding="utf-8") as f:
        for j, p in sorted(recordes.items(), key=lambda x: x[1], reverse=True):
            f.write(f"{j}:{p}\n")


def exibir_tabela_recordes(caminho=ARQUIVO_RECORDES):
    recordes = carregar_recordes(caminho)
    print("\n=== Ranking de Recordes ===")
    if not recordes:
        print("Nenhum recorde registrado.")
        return

    for posicao, (j, p) in enumerate(
        sorted(recordes.items(), key=lambda x: x[1], reverse=True), start=1
    ):
        print(f"{posicao:02d}. {j:15s} - {p} pontos")


if __name__ == "__main__":
    arq_temp = "temp_recordes_demo.txt"
    salvar_recorde("Alice", 10, arq_temp)
    salvar_recorde("Bob", 15, arq_temp)
    salvar_recorde("Alice", 18, arq_temp)  # Atualização de Alice

    exibir_tabela_recordes(arq_temp)

    if os.path.exists(arq_temp):
        os.remove(arq_temp)
