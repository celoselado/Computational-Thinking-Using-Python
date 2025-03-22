## Exercicio 1= Escreva um algoritmo para calcular o estoque médio de uma peça, sendo
## que: estoque médio = (quantidade mínima + quantidade máxima) / 2

nome = input("Digite o seu nome:")

qnt_minima = int(input("Digite a quantidade minima de peças:"))
qnt_maxima = int(input("Agora digite a quantidade maxima de peças:"))

media_peças = (qnt_minima + qnt_maxima) / 2

print("Sr(a)",nome,"a quantidade média do estoque é de: ", media_peças)