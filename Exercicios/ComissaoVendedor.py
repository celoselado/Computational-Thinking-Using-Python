# Exercicio 6 = Crie um algoritmo para calcular o pagamento de comissão de vendedores
# de peças, levando em consideração que sua comissão será de 5% do total
# da venda e que você tem os seguintes dados:
# - identificação do vendedor
# - código da peça
# - preço unitário da peça
# - quantidade vendida
# O algoritmo deve imprimir a identificação do vendedor, o total vendido pelo
# vendedor e o valor da comissão da venda.

codigo_peça = 24665343
preco_unitario =  54.67
condicao = "Nao"

nome = input("Bem vindo ao sistema, vendedor! Digite o seu nome por favor: ")

qnt_pecas = int(input("Quantas peças serão vendidas? Digite a quantidade: "))

valor_total = qnt_pecas * preco_unitario

comissao = valor_total * 0.05

print("O valor unitário da peça é",preco_unitario," e o valor total ficou R$",valor_total,"e a comissão que voce ira receber pela venda é de R$",(round(comissao, 2)))









