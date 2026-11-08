"""
Exercício 10.5 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Adicione atributos e métodos à classe Televisao para controlar o volume:
atributo volume (iniciado em valor padrão, ex.: 10), limite mínimo (0)
e limite máximo (100), além dos métodos aumenta_volume e diminui_volume.
"""


class Televisao:
    def __init__(
        self, canal_min=2, canal_max=14, volume_inicial=10, vol_min=0, vol_max=100
    ):
        self.canal_min = canal_min
        self.canal_max = canal_max
        self.canal = canal_min
        self.vol_min = vol_min
        self.vol_max = vol_max
        self.volume = volume_inicial

    def aumenta_volume(self):
        if self.volume < self.vol_max:
            self.volume += 1

    def diminui_volume(self):
        if self.volume > self.vol_min:
            self.volume -= 1


if __name__ == "__main__":
    tv = Televisao(volume_inicial=99, vol_max=100)
    print(f"Volume inicial: {tv.volume}")

    tv.aumenta_volume()
    print(f"Após aumentar: {tv.volume}")

    tv.aumenta_volume()  # Tentando ultrapassar o máximo
    print(f"Tentativa de aumentar além do máximo (100): {tv.volume}")

    tv.diminui_volume()
    print(f"Após diminuir: {tv.volume}")
