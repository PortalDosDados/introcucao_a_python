"""
Exercício 10.1 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Adicione os atributos tamanho e marca à classe Televisao. Crie dois objetos
do tipo Televisao com tamanhos e marcas diferentes e imprima seus valores.
"""


class Televisao:
    def __init__(self, canal=2, tamanho=32, marca="Genérica"):
        self.ligada = False
        self.canal = canal
        self.tamanho = tamanho
        self.marca = marca


if __name__ == "__main__":
    tv1 = Televisao(canal=4, tamanho=42, marca="Sony")
    tv2 = Televisao(canal=7, tamanho=55, marca="Samsung")

    print(f'TV 1 -> Marca: {tv1.marca}, Tamanho: {tv1.tamanho}", Canal: {tv1.canal}')
    print(f'TV 2 -> Marca: {tv2.marca}, Tamanho: {tv2.tamanho}", Canal: {tv2.canal}')
