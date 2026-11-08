"""
Exercício 10.4 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Modifique os métodos muda_canal_para_cima e muda_canal_para_baixo da classe
Televisao para utilizarem a rotação circular de canais entre o mínimo e o máximo.
"""


class Televisao:
    def __init__(self, canal_min=2, canal_max=14):
        self.canal_min = canal_min
        self.canal_max = canal_max
        self.canal = canal_min

    def muda_canal_para_cima(self):
        if self.canal + 1 > self.canal_max:
            self.canal = self.canal_min
        else:
            self.canal += 1

    def muda_canal_para_baixo(self):
        if self.canal - 1 < self.canal_min:
            self.canal = self.canal_max
        else:
            self.canal -= 1


if __name__ == "__main__":
    tv = Televisao(canal_min=2, canal_max=5)
    print(f"Canal inicial: {tv.canal}")

    tv.muda_canal_para_baixo()
    print(f"Muda para baixo a partir do canal mínimo -> Canal: {tv.canal}")

    tv.muda_canal_para_cima()
    print(f"Muda para cima a partir do canal máximo -> Canal: {tv.canal}")
