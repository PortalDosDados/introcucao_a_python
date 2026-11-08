"""
Exercício 10.9 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Crie uma classe Cidade com nome e população. Em seguida, crie uma classe Estado
com nome, sigla e uma lista de cidades. Adicione um método à classe Estado que
calcule a população total do estado somando a população de suas cidades
(demonstrando o conceito de composição e agregação de objetos).
"""


class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao


class Estado:
    def __init__(self, nome, sigla, cidades=None):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades if cidades is not None else []

    def adicionar_cidade(self, cidade):
        self.cidades.append(cidade)

    def populacao_total(self):
        total = 0
        for cidade in self.cidades:
            total += cidade.populacao
        return total


if __name__ == "__main__":
    c1 = Cidade("Curitiba", 1963726)
    c2 = Cidade("Londrina", 575377)
    c3 = Cidade("Maringá", 430157)

    parana = Estado(nome="Paraná", sigla="PR", cidades=[c1, c2])
    parana.adicionar_cidade(c3)

    print(f"Estado: {parana.nome} ({parana.sigla})")
    print(f"Cidades cadastradas ({len(parana.cidades)}):")
    for cid in parana.cidades:
        print(f"  - {cid.nome}: {cid.populacao:,} habitantes")

    print(f"População total calculada: {parana.populacao_total():,} habitantes")
