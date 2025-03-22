## Exercicio 5= Escreva um algoritmo que leia a cotação do dólar e a quantidade de
## dólares a ser comprada. Converta o valor para real e mostre o resultado

cotacao_dolar = 5.73

valor_dolar = float(input("A cotação atual do dolar em reais é de R$ 5.73 quantos dolares você gostaria de comprar? Digete o valor: "))

valor_real = valor_dolar * cotacao_dolar

print("Comprando",valor_dolar,"dolares você terá que pagar R$",valor_real)