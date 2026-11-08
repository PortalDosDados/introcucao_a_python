"""
Exercício 8.9 - Livro: Introdução à Programação com Python (Nilo Ney Coutinho Menezes)

Enunciado:
Rastreie o Programa 8.3 (fatorial recursivo). O que acontece se chamarmos a
função fatorial com -1? Altere a função fatorial para exibir o nível de
recursão a cada chamada e retorno, e trate entradas inválidas (números negativos).
"""


def fatorial(n, nivel=1):
    espaco = "  " * (nivel - 1)
    print(f"{espaco}fatorial({n}) calculando...")

    if n < 0:
        print(f"{espaco}Erro: Fatorial não definido para números negativos.")
        return None
    if n == 0 or n == 1:
        print(f"{espaco}fatorial({n}) = 1 (caso base)")
        return 1

    resultado = n * fatorial(n - 1, nivel + 1)
    print(f"{espaco}fatorial({n}) retornou {resultado}")
    return resultado


# Demonstração e testes
if __name__ == "__main__":
    print("--- Rastreamento de fatorial(4) ---")
    res = fatorial(4)
    print(f"Resultado final: {res}\n")

    print("--- Teste com número negativo: fatorial(-1) ---")
    res_neg = fatorial(-1)
    print(f"Resultado final: {res_neg}")
