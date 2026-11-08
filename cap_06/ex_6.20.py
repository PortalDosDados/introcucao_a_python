"""
Exercício 6.20 Escreva um programa que compare duas listas. Utilizando operações
com conjuntos (set), encontre:
- Os elementos que não mudaram (presentes em ambas as versões)
- Os novos elementos (adicionados na versão final)
- Os elementos que foram removidos (presentes apenas na versão inicial)
"""

versao_inicial = [1, 2, 3, 4, 5]
versao_final = [3, 4, 5, 6, 7]

conjunto_inicial = set(versao_inicial)
conjunto_final = set(versao_final)

nao_mudaram = conjunto_inicial & conjunto_final
novos_elementos = conjunto_final - conjunto_inicial
removidos = conjunto_inicial - conjunto_final

print(f"Versão inicial: {versao_inicial}")
print(f"Versão final:   {versao_final}")
print(f"Elementos que não mudaram: {nao_mudaram}")
print(f"Novos elementos adicionados: {novos_elementos}")
print(f"Elementos que foram removidos: {removidos}")
