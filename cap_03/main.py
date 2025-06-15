# A função input retorna uma string, então precisamos converter para float 

'''

salario = input("Digite o salário: ")
idade = input("Digite a idade: ")

if float(salario) > 1000 and int(idade) < 25:
    print("Emprestimo aprovado")
else:
    print("Emprestimo negado")
'''
'''
nome = input("Digite seu nome:") 
print(f'Você digitou, {nome}')
'''

#script para calcular o bônus de um funcionário
anos = int(input("Anos de serviço: ")) #variável anos recebe um valor inteiro
valor_por_ano = float(input("Valor por ano: ")) #variável valor_por_ano recebe um valor float
bônus = anos * valor_por_ano #cálculo do bônus
print(f'Bônus de R$ {bônus} bônus') #imprime o bônus calculado