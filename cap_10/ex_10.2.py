"""
Exercício 10.2 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Modifique a classe Televisao de forma que os canais mínimo e máximo sejam
passados na inicialização do construtor __init__.
"""


class Televisao:
    def __init__(self, canal_min=2, canal_max=14, tamanho=32, marca="Genérica"):
        self.ligada = False
        self.canal_min = canal_min
        self.canal_max = canal_max
        self.canal = canal_min
        self.tamanho = tamanho
        self.marca = marca


if __name__ == "__main__":
    tv_antena = Televisao(canal_min=2, canal_max=13, tamanho=40, marca="LG")
    tv_cabo = Televisao(canal_min=1, canal_max=99, tamanho=65, marca="Philips")

    print(
        f"TV Antena: Faixa de canais {tv_antena.canal_min} até {tv_antena.canal_max} (Canal atual: {tv_antena.canal})"
    )
    print(
        f"TV Cabo: Faixa de canais {tv_cabo.canal_min} até {tv_cabo.canal_max} (Canal atual: {tv_cabo.canal})"
    )
