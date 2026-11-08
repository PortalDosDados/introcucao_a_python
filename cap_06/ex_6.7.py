"""
Exercício 6.7 Faça um programa que leia uma expressão com parênteses. Usando
pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
Exemplos:
(())      -> OK
()()(())  -> OK
())       -> Erro
)(        -> Erro
"""

expressao = input("Digite a expressão com parênteses: ")
pilha = []
correto = True

for caractere in expressao:
    if caractere == "(":
        pilha.append("(")
    elif caractere == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            correto = False
            break

if correto and len(pilha) == 0:
    print("Expressão com parênteses balanceados e corretos!")
else:
    print("Erro! A quantidade ou ordem dos parênteses está incorreta.")
