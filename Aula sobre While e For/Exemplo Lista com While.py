'''
Crie um programa em python que recebe como entrada quatro salário, o programa deve calcular a media salarial e exibir os salarios que estão abaixo da média usando Lista e Laço de repetição while
'''

soma = 0
salarios = [0,0,0,0]
i = 0   #Controle do looping

while i < 4:
    salarios[i] = float(input('Salario R$:'))
    soma += salarios[i]
    i+=1    

media = soma/4

i = 0 # Controle do laço de repetição
while i < 4:
    if salarios[i] < media:
        print(f'Salário {i} {salarios[i]:.2f} é menor que a média')
    i+=1