'''
Crie um programa em python que recebe como entrada quatro salário, o programa deve calcular a media salarial e exibir os salarios que estão abaixo da média usando Lista e Laço de repetição FOR
'''

salarios = []
soma = 0

for i in range(4): 
    salario = float(input('Salário R$:'))
    soma += salario
    salarios.append(salario) #Adiciona salario na lista Salarios.

media = soma/4

print(f'Média: {media}')
for salario in salarios:
    if salario < media:
        print(f'Salário: {salario:.2f}')


