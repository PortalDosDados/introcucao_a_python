"""
Exercício 10.3 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Modifique a classe Televisao de forma que, se tentarmos mudar para um canal
menor que o canal mínimo, o canal atual vá para o canal máximo, e se tentarmos
mudar para um canal maior que o máximo, vá para o canal mínimo (comportamento cíclico).
"""


class Televisao:
    def __init__(self, canal_min=2, canal_max=14):
        self.canal_min = canal_min
        self.canal_max = canal_max
        self.canal = canal_min

    def ajusta_canal(self, novo_canal):
        if novo_canal < self.canal_min:
            self.canal = self.canal_max
        elif novo_canal > self.canal_max:
            self.canal = self.canal_min
        else:
            self.canal = novo_canal


if __name__ == "__main__":
    tv = Televisao(canal_min=2, canal_max=10)
    print(f"Canal inicial: {tv.canal}")

    # Testando abaixo do mínimo
    tv.ajusta_canal(1)
    print(f"Tentativa de ir para canal 1 (abaixo do mín 2) -> Foi para: {tv.canal}")

    # Testando acima do máximo
    tv.ajusta_canal(11)
    print(f"Tentativa de ir para canal 11 (acima do máx 10) -> Foi para: {tv.canal}")
